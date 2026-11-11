from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name="py_bronze")
def py_bronze():
    return spark.readStream.table("workspace.water_monitoring.water_meter_readings_source")

@dp.table(name="py_silver")
def py_silver():
    return (spark.readStream.table("py_bronze")
            .filter("reading_status='Valid' AND flow_lpm>0 AND consumption_liters>0"))

@dp.materialized_view(name="py_gold_zone")
def py_gold_zone():
    return (spark.read.table("py_silver").groupBy("zone_id")
            .agg(F.sum("consumption_liters").alias("total_consumption"),
                 F.avg("pressure_bar").alias("avg_pressure"),
                 F.count("*").alias("reading_count")))