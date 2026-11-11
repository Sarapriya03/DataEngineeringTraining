-- BRONZE: raw readings (streaming, append-only source) and zone master
CREATE OR REFRESH STREAMING TABLE cap_bronze_readings AS
SELECT * FROM STREAM(workspace.water_monitoring.water_meter_readings_source);

CREATE OR REFRESH MATERIALIZED VIEW cap_bronze_zones AS
SELECT * FROM workspace.water_monitoring.water_zones;

-- SILVER: valid readings with positive measurements plus concern flags
CREATE OR REFRESH STREAMING TABLE cap_silver_readings AS
SELECT *,
       COALESCE(pressure_bar < 2.5, false) AS low_pressure_flag,
       (pressure_bar IS NULL OR source_system IS NULL OR zone_id IS NULL) AS quality_flag
FROM STREAM(cap_bronze_readings)
WHERE reading_status = 'Valid' AND flow_lpm > 0 AND consumption_liters > 0;

-- GOLD 1: clean readings, one row per reading_id, enriched with zone info
CREATE OR REFRESH MATERIALIZED VIEW cap_gold_clean_readings AS
SELECT r.*, z.zone_name, z.district,
       (z.zone_id IS NULL) AS unknown_zone_flag
FROM (
  SELECT * EXCEPT (rn) FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY reading_id
              ORDER BY reading_time DESC, source_system) AS rn
    FROM cap_silver_readings)
  WHERE rn = 1) r
LEFT JOIN cap_bronze_zones z ON r.zone_id = z.zone_id;

-- GOLD 2: per-zone summary
CREATE OR REFRESH MATERIALIZED VIEW cap_gold_zone_summary AS
SELECT zone_id, zone_name, district,
       SUM(consumption_liters) AS total_consumption,
       AVG(pressure_bar)       AS avg_pressure,
       COUNT(*)                AS reading_count,
       COUNT_IF(low_pressure_flag) AS low_pressure_readings,
       COUNT_IF(quality_flag)      AS quality_concern_readings
FROM cap_gold_clean_readings
GROUP BY zone_id, zone_name, district;

-- GOLD 3: per-district summary
CREATE OR REFRESH MATERIALIZED VIEW cap_gold_district_summary AS
SELECT district,
       SUM(consumption_liters) AS total_consumption,
       AVG(pressure_bar)       AS avg_pressure,
       COUNT(*)                AS reading_count,
       COUNT_IF(low_pressure_flag) AS low_pressure_readings,
       COUNT_IF(quality_flag)      AS quality_concern_readings
FROM cap_gold_clean_readings
WHERE district IS NOT NULL
GROUP BY district;