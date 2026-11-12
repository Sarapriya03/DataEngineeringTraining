from datetime import datetime, timedelta

try:
    from airflow.sdk import DAG
except ImportError:
    from airflow import DAG

from airflow.providers.standard.operators.python import (
    PythonOperator, BranchPythonOperator
)


def load_incident():
    incident = {
        "ticket_id": "INC-402",
        "service": "Email",
        "severity": "High",
        "reported_by": "Operations",
    }
    return incident


def choose_response(ti):
    incident = ti.xcom_pull(task_ids="load_incident")
    severity = incident["severity"]
    print(f"Incident {incident['ticket_id']} severity: {severity}")
    if severity in ("High", "Critical"):
        return "urgent_response"
    return "standard_response"


def urgent_response(ti):
    incident = ti.xcom_pull(task_ids="load_incident")
    attempt = ti.try_number
    print(f"Urgent response, attempt number: {attempt}")
    if attempt == 1:
        raise Exception("Simulated temporary failure on first attempt")
    print(
        f"ESCALATION: {incident['ticket_id']} ({incident['service']}) "
        f"escalated to on-call engineer. Reported by {incident['reported_by']}."
    )


def standard_response():
    print("Ticket assigned to the standard service desk queue.")


def write_audit(ti):
    incident = ti.xcom_pull(task_ids="load_incident")
    print(f"Audit: incident {incident['ticket_id']} processing completed.")


with DAG(
    dag_id="it_incident_routing_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["practice"],
) as dag:

    load_incident_task = PythonOperator(
        task_id="load_incident",
        python_callable=load_incident,
    )

    choose_response_task = BranchPythonOperator(
        task_id="choose_response",
        python_callable=choose_response,
    )

    urgent_task = PythonOperator(
        task_id="urgent_response",
        python_callable=urgent_response,
        retries=1,
        retry_delay=timedelta(seconds=10),
    )

    standard_task = PythonOperator(
        task_id="standard_response",
        python_callable=standard_response,
    )

    audit_task = PythonOperator(
        task_id="write_audit",
        python_callable=write_audit,
        trigger_rule="none_failed_min_one_success",
    )

    load_incident_task >> choose_response_task
    choose_response_task >> [urgent_task, standard_task]
    [urgent_task, standard_task] >> audit_task
