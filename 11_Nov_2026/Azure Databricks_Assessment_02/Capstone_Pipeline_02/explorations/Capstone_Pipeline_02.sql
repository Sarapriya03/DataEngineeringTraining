-- Databricks notebook source
SELECT * FROM workspace.water_monitoring.cap_gold_zone_summary
ORDER BY total_consumption DESC;

-- COMMAND ----------

SELECT * FROM workspace.water_monitoring.cap_gold_district_summary;

-- COMMAND ----------

SELECT COUNT(*), COUNT(DISTINCT reading_id)
FROM workspace.water_monitoring.cap_gold_clean_readings;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Part 2: One MERGE**

-- COMMAND ----------

MERGE INTO workspace.water_monitoring.water_meter_readings_work t
USING workspace.water_monitoring.water_reading_changes s ON t.reading_id = s.reading_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;

-- COMMAND ----------

SELECT s.reading_id, s.flow_lpm AS new_flow, t.flow_lpm AS table_flow
FROM workspace.water_monitoring.water_reading_changes s JOIN workspace.water_monitoring.water_meter_readings_work t USING (reading_id);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Part 3: One historical Delta query**

-- COMMAND ----------

DESCRIBE HISTORY workspace.water_monitoring.water_meter_readings_work;

-- COMMAND ----------

SELECT * FROM workspace.water_monitoring.water_meter_readings_work VERSION AS OF 3 WHERE reading_id=1005;

-- COMMAND ----------

SELECT * FROM workspace.water_monitoring.water_meter_readings_work WHERE reading_id = 1005;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Four visualizations**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **1.Bar: consumption by zone**

-- COMMAND ----------

SELECT zone_name, total_consumption FROM workspace.water_monitoring.cap_gold_zone_summary

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **2.Pie: consumption share by district**

-- COMMAND ----------

SELECT district, total_consumption FROM workspace.water_monitoring.cap_gold_district_summary

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **3.Line: daily consumption**

-- COMMAND ----------

SELECT CAST(reading_time AS DATE) reading_date, SUM(consumption_liters) daily_consumption FROM workspace.water_monitoring.cap_gold_clean_readings GROUP BY 1 ORDER BY 1

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **4.Scatter: pressure vs flow**

-- COMMAND ----------

SELECT pressure_bar, flow_lpm FROM workspace.water_monitoring.cap_gold_clean_readings