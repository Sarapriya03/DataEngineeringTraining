# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC DROP MATERIALIZED VIEW IF EXISTS workspace.themepark.tp_cap_gold;
# MAGIC DROP TABLE IF EXISTS workspace.themepark.tp_cap_silver;
# MAGIC DROP TABLE IF EXISTS workspace.themepark.tp_cap_bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.themepark.tp_cap_gold
# MAGIC ORDER BY total_revenue DESC;