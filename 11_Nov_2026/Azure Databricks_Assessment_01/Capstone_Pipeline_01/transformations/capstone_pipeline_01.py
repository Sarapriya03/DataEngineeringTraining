from pyspark import pipelines as dp
from pyspark.sql import functions as F

# BRONZE: raw, append-only source, no changes
@dp.table(name="tp_cap_bronze", comment="Raw visitor entries")
def tp_cap_bronze():
    return spark.readStream.table("workspace.themepark.tp_entries_raw")

# SILVER: validate, dedupe, fill channel, calculate revenue
@dp.table(name="tp_cap_silver", comment="Validated completed entries")
def tp_cap_silver():
    return (
        spark.readStream.table("tp_cap_bronze")
        .filter("status = 'Completed'")
        .filter("ticket_price > 0")
        .filter("wait_minutes >= 0")
        .filter("ride_minutes > 0")
        .filter("attraction_id IS NOT NULL")
        .dropDuplicates(["entry_id"])
        .withColumn("booking_channel", F.coalesce("booking_channel", F.lit("Unknown")))
        .withColumn("visit_date", F.to_date("visit_date"))
        .withColumn("revenue", F.col("ticket_price").cast("double"))
    )

# GOLD: entries, revenue, avg wait by attraction and zone
@dp.materialized_view(name="tp_cap_gold", comment="KPIs by attraction and zone")
def tp_cap_gold():
    s = spark.read.table("tp_cap_silver")
    a = spark.read.table("workspace.themepark.tp_attractions")
    return (
        s.join(a, "attraction_id", "inner")      # inner join also drops orphan IDs
         .groupBy("attraction_id", "attraction_name", F.col("location.zone").alias("zone"))
         .agg(F.count("*").alias("entries"),
              F.round(F.sum("revenue"), 2).alias("total_revenue"),
              F.round(F.avg("wait_minutes"), 1).alias("avg_wait_minutes"))
    )
