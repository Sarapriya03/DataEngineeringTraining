# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC USE CATALOG workspace;
# MAGIC USE SCHEMA water_monitoring;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE gold_before_incremental AS
# MAGIC SELECT * FROM water_gold_zone;
# MAGIC
# MAGIC SELECT SUM(reading_count) AS total_readings,
# MAGIC        SUM(total_consumption) AS total_consumption
# MAGIC FROM gold_before_incremental;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM water_meter_readings_source;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   (SELECT SUM(reading_count) FROM gold_before_incremental) AS before_count,  
# MAGIC   (SELECT SUM(reading_count) FROM water_gold_zone)         AS after_count,
# MAGIC   (SELECT SUM(total_consumption) FROM gold_before_incremental) AS before_consumption,
# MAGIC   (SELECT SUM(total_consumption) FROM water_gold_zone)         AS after_consumption;