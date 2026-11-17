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
def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('Baggage records loaded:', len(records))
    return records


# ---------- Task 2: identify bags requiring manual review ----------
def identify_review_bags(ti):
    records = ti.xcom_pull(task_ids="load_baggage")

    review_bags = []
    for rec in records:
        weight = int(rec["weight_kg"])
        status = rec["screening_status"].strip()
        print(f"{rec['bag_id']} ({rec['flight_no']}): weight={weight}kg, status={status}")

        # screening_status is Review OR weight_kg is greater than 23
        if status == "Review" or weight > 23:
            review_bags.append(rec["bag_id"])

    print("Bags requiring review:", review_bags)
    return review_bags


# ---------- Task 3: total baggage weight ----------
def calculate_total_weight(ti):
    records = ti.xcom_pull(task_ids="load_baggage")

    total_weight = sum(int(rec["weight_kg"]) for rec in records)

    print("Total baggage weight (kg):", total_weight)
    return total_weight


# ---------- Task 4: final report ----------
def generate_report(ti):
    records = ti.xcom_pull(task_ids="load_baggage")
    review_bags = ti.xcom_pull(task_ids="identify_review_bags")
    total_weight = ti.xcom_pull(task_ids="calculate_total_weight")

    print("=" * 40)
    print("AIRPORT BAGGAGE SCREENING REPORT")
    print("=" * 40)
    print("Number of bags             :", len(records))
    print("Bags requiring review      :", ", ".join(review_bags) if review_bags else "None")
    print("Total baggage weight (kg)  :", total_weight)
    print("=" * 40)


# ---------- DAG definition ----------
with DAG(
    dag_id="airport_baggage_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["assessment", "airport"],
) as dag:

    load_task = PythonOperator(
        task_id="load_baggage",
        python_callable=load_baggage,
    )

    review_task = PythonOperator(
        task_id="identify_review_bags",
        python_callable=identify_review_bags,
    )

    weight_task = PythonOperator(
        task_id="calculate_total_weight",
        python_callable=calculate_total_weight,
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    # load_baggage -> [identify_review_bags || calculate_total_weight] -> generate_report
    load_task >> [review_task, weight_task] >> report_task