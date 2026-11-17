import csv
from datetime import datetime

from airflow import DAG

try:
    # Airflow 3.x
    from airflow.providers.standard.operators.python import PythonOperator
except ImportError:
    # Airflow 2.x
    from airflow.operators.python import PythonOperator


# ---------- Task 1: starter function (provided) ----------
def load_batches():
    with open("/opt/airflow/dags/factory_batches.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    print("Batches loaded:", len(rows))
    return rows


# ---------- Task 2: quality check ----------
def check_quality(ti):
    rows = ti.xcom_pull(task_ids="load_batches")

    review_batches = []
    for row in rows:
        units = int(row["units_produced"])
        defects = int(row["defective_units"])
        defect_rate = defects / units * 100
        print(f"{row['batch_id']}: defect rate = {defect_rate:.2f}%")

        # defective units exceed 5% of units produced
        if defects > 0.05 * units:
            review_batches.append(row["batch_id"])

    print("Batches requiring review:", review_batches)
    return review_batches


# ---------- Task 3: production value ----------
def calculate_value(ti):
    rows = ti.xcom_pull(task_ids="load_batches")

    total_value = 0
    for row in rows:
        units = int(row["units_produced"])
        price = int(row["value_per_unit"])
        batch_value = units * price
        print(f"{row['batch_id']}: value = {batch_value}")
        total_value += batch_value

    print("Total production value:", total_value)
    return total_value


# ---------- Task 4: final report ----------
def generate_report(ti):
    rows = ti.xcom_pull(task_ids="load_batches")
    review_batches = ti.xcom_pull(task_ids="check_quality")
    total_value = ti.xcom_pull(task_ids="calculate_value")

    print("=" * 40)
    print("MANUFACTURING BATCH QUALITY REPORT")
    print("=" * 40)
    print("Total number of batches    :", len(rows))
    print("Batches requiring review   :", ", ".join(review_batches) if review_batches else "None")
    print("Total production value     :", total_value)
    print("=" * 40)


# ---------- DAG definition ----------
with DAG(
    dag_id="factory_quality_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["assessment", "manufacturing"],
) as dag:

    load_task = PythonOperator(
        task_id="load_batches",
        python_callable=load_batches,
    )

    quality_task = PythonOperator(
        task_id="check_quality",
        python_callable=check_quality,
    )

    value_task = PythonOperator(
        task_id="calculate_value",
        python_callable=calculate_value,
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    # load_batches -> [check_quality || calculate_value] -> generate_report
    load_task >> [quality_task, value_task] >> report_task