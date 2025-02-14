from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def get_user_data():
    print("Получение данных от пользователей")

def generate_user_attributes():
    print("Генерация данных для пользователей")

def populate_database():
    print("Наполнение базы данных изображениями собственности")

def download_images():
    print("Скачивание изображений собственности")

def train_model():
    print("Тренировка модели машинного обучения")

def assign_credit_category():
    print("Присвоение категории платежеспособности")

def update_database():
    print("Обновление записи пользователя в базе данных")

default_args = {
    'owner': 'Софья (@honeymi), Николай (@NickAllenov), Дмитрий (@aldmikon27), Дарина (@Belladonna_103), \
              Ильнар (@Ilnarq), Никита (@nikitamikhel), Иван (@imtl34), Оксана (@kaledinaoa), Андрей (@AndrewLuferenko)',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'assessment_dag_demo',
    default_args=default_args,
    description='DAG для оценки платежеспособности клиентов',
    schedule_interval='@daily',
    tags=['PET-Solvency-Assessment']
)

get_user_data_task = PythonOperator(
    task_id='get_user_data',
    python_callable=get_user_data,
    dag=dag,
)

generate_user_attributes_task = PythonOperator(
    task_id='generate_user_attributes',
    python_callable=generate_user_attributes,
    dag=dag,
)

populate_database_task = PythonOperator(
    task_id='populate_database',
    python_callable=populate_database,
    dag=dag,
)

download_images_task = PythonOperator(
    task_id='download_images',
    python_callable=download_images,
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

assign_credit_category_task = PythonOperator(
    task_id='assign_credit_category',
    python_callable=assign_credit_category,
    dag=dag,
)

update_database_task = PythonOperator(
    task_id='update_database',
    python_callable=update_database,
    dag=dag,
)

# Определение порядка выполнения задач
get_user_data_task >> generate_user_attributes_task >> populate_database_task
populate_database_task >> download_images_task >> train_model_task
train_model_task >> assign_credit_category_task >> update_database_task
