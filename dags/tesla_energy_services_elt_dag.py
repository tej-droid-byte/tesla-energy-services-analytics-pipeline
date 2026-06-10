from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_DIR = "/opt/airflow/tesla_energy_services_analytics_pipeline"

default_args = {
    "owner": "tej-more",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="tesla_energy_services_elt_pipeline",
    description="Python + SQL ELT pipeline for energy services operational analytics and Tableau dashboards",
    default_args=default_args,
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=["python", "sql", "elt", "airflow", "tableau", "operations-analytics"],
) as dag:

    extract_transform_load = BashOperator(
        task_id="extract_transform_load_service_tickets",
        bash_command=f"cd {PROJECT_DIR} && python src/etl_pipeline.py",
    )

    run_sql_kpi_transforms = BashOperator(
        task_id="run_sql_kpi_transforms",
        bash_command=f"cd {PROJECT_DIR} && python src/run_sql_transforms.py",
    )

    export_tableau_dataset = BashOperator(
        task_id="export_tableau_dashboard_dataset",
        bash_command=f"test -f {PROJECT_DIR}/tableau/tesla_energy_services_dashboard_data.csv",
    )

    extract_transform_load >> run_sql_kpi_transforms >> export_tableau_dataset
