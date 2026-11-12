from datetime import datetime

try:
    from airflow.sdk import DAG
except ImportError:
    from airflow import DAG

from airflow.providers.standard.operators.python import PythonOperator


def load_rooms():
    rooms = [
        {"room": 101, "status": "Ready", "cleaning_min": 0},
        {"room": 102, "status": "Cleaning", "cleaning_min": 25},
        {"room": 103, "status": "Ready", "cleaning_min": 0},
        {"room": 104, "status": "Cleaning", "cleaning_min": 40},
        {"room": 105, "status": "Cleaning", "cleaning_min": 30},
    ]
    return rooms


def find_rooms_to_clean(ti):
    rooms = ti.xcom_pull(task_ids="load_rooms")
    to_clean = [r["room"] for r in rooms if r["status"] == "Cleaning"]
    print(f"Rooms needing cleaning: {to_clean}")
    return to_clean


def calculate_cleaning_minutes(ti):
    rooms = ti.xcom_pull(task_ids="load_rooms")
    total = sum(r["cleaning_min"] for r in rooms if r["status"] == "Cleaning")
    print(f"Total cleaning minutes: {total}")
    return total


def generate_housekeeping_report(ti):
    rooms_to_clean = ti.xcom_pull(task_ids="find_rooms_to_clean")
    total_minutes = ti.xcom_pull(task_ids="calculate_cleaning_minutes")
    print("=" * 40)
    print("HOUSEKEEPING SUMMARY")
    print("=" * 40)
    print(f"Rooms needing cleaning : {rooms_to_clean}")
    print(f"Number of rooms        : {len(rooms_to_clean)}")
    print(f"Total cleaning time    : {total_minutes} minutes")
    print("=" * 40)


with DAG(
    dag_id="hotel_readiness_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["practice"],
) as dag:

    load_rooms_task = PythonOperator(
        task_id="load_rooms",
        python_callable=load_rooms,
    )

    find_rooms_task = PythonOperator(
        task_id="find_rooms_to_clean",
        python_callable=find_rooms_to_clean,
    )

    calc_minutes_task = PythonOperator(
        task_id="calculate_cleaning_minutes",
        python_callable=calculate_cleaning_minutes,
    )

    report_task = PythonOperator(
        task_id="generate_housekeeping_report",
        python_callable=generate_housekeeping_report,
    )

    load_rooms_task >> [find_rooms_task, calc_minutes_task]
    [find_rooms_task, calc_minutes_task] >> report_task
