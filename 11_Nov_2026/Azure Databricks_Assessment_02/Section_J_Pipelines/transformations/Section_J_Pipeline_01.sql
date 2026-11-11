CREATE OR REFRESH STREAMING TABLE water_bronze AS
SELECT * FROM STREAM(workspace.water_monitoring.water_meter_readings_source);

CREATE OR REFRESH STREAMING TABLE water_silver AS
SELECT * FROM STREAM(water_bronze)
WHERE reading_status='Valid' AND flow_lpm>0 AND consumption_liters>0;

CREATE OR REFRESH MATERIALIZED VIEW water_gold_zone AS
SELECT zone_id, SUM(consumption_liters) total_consumption,
       AVG(pressure_bar) avg_pressure, COUNT(*) reading_count
FROM water_silver GROUP BY zone_id;