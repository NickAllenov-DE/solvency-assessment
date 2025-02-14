from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Функции для имитации работы задач
def install_app():
    print("Установка приложения на телефон пользователя.")

def request_permissions():
    print("Запрос разрешений на доступ к галерее и камере.")

def scan_gallery_for_images():
    print("Сканирование галереи для получения изображений.")

def evaluate_images_with_ml_model():
    print("Оценка изображений с помощью ML моделей для определения платежеспособности.")

def generate_solvency_score():
    print("Генерация итоговой оценки платежеспособности на основе результатов изображений.")

def update_user_profile():
    print("Обновление профиля пользователя в базе данных с оценкой платежеспособности.")

def recommend_bank_products():
    print("Рекомендация банковских продуктов на основе оценки платежеспособности.")

# Аргументы по умолчанию для DAG
default_args = {
    'owner': 'Team Solvency',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'bank_application_process',
    default_args=default_args,
    description='DAG для имитации процесса работы банковского приложения',
    schedule_interval='@daily',
    tags=['Bank', 'SolvencyAssessment', 'Demo'],
)

# Задачи
install_app_task = PythonOperator(
    task_id='install_app',
    python_callable=install_app,
    dag=dag,
)

request_permissions_task = PythonOperator(
    task_id='request_permissions',
    python_callable=request_permissions,
    dag=dag,
)

scan_gallery_for_images_task = PythonOperator(
    task_id='scan_gallery_for_images',
    python_callable=scan_gallery_for_images,
    dag=dag,
)

evaluate_images_with_ml_model_task = PythonOperator(
    task_id='evaluate_images_with_ml_model',
    python_callable=evaluate_images_with_ml_model,
    dag=dag,
)

generate_solvency_score_task = PythonOperator(
    task_id='generate_solvency_score',
    python_callable=generate_solvency_score,
    dag=dag,
)

update_user_profile_task = PythonOperator(
    task_id='update_user_profile',
    python_callable=update_user_profile,
    dag=dag,
)

recommend_bank_products_task = PythonOperator(
    task_id='recommend_bank_products',
    python_callable=recommend_bank_products,
    dag=dag,
)

# Определение порядка выполнения задач
install_app_task >> request_permissions_task >> scan_gallery_for_images_task
scan_gallery_for_images_task >> evaluate_images_with_ml_model_task >> generate_solvency_score_task
generate_solvency_score_task >> update_user_profile_task >> recommend_bank_products_task
