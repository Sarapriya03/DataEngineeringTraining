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
def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('ATM records loaded:', len(records))
    return records


# ---------- Task 2: identify ATMs with low cash ----------
def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids="load_atms")

    low_cash_atms = []
    for rec in records:
        cash = int(rec["cash_available"])
        demand = int(rec["daily_demand"])
        print(f"{rec['atm_id']} ({rec['location']}): cash={cash}, demand={demand}")

        # cash_available is less than daily_demand
        if cash < demand:
            low_cash_atms.append(rec["atm_id"])

    print("Low-cash ATMs:", low_cash_atms)
    return low_cash_atms


# ---------- Task 3: total cash across all ATMs ----------
def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids="load_atms")

    total_cash = sum(int(rec["cash_available"]) for rec in records)

    print("Total cash available:", total_cash)
    return total_cash


# ---------- Task 4: final report ----------
def generate_report(ti):
    records = ti.xcom_pull(task_ids="load_atms")
    low_cash_atms = ti.xcom_pull(task_ids="identify_low_cash")
    total_cash = ti.xcom_pull(task_ids="calculate_total_cash")

    print("=" * 40)
    print("ATM CASH REPLENISHMENT REPORT")
    print("=" * 40)
    print("Number of ATMs             :", len(records))
    print("Low-cash ATM IDs           :", ", ".join(low_cash_atms) if low_cash_atms else "None")
    print("Total available cash       :", total_cash)
    print("=" * 40)


# ---------- DAG definition ----------
with DAG(
    dag_id="atm_cash_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["assessment", "banking"],
) as dag:

    load_task = PythonOperator(
        task_id="load_atms",
        python_callable=load_atms,
    )

    low_cash_task = PythonOperator(
        task_id="identify_low_cash",
        python_callable=identify_low_cash,
    )

    total_cash_task = PythonOperator(
        task_id="calculate_total_cash",
        python_callable=calculate_total_cash,
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    # load_atms -> [identify_low_cash || calculate_total_cash] -> generate_report
    load_task >> [low_cash_task, total_cash_task] >> report_task