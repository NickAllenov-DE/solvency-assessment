
-- Создаем базу и пользователя для Airflow
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'airflow') THEN
        CREATE DATABASE airflow;
        CREATE USER airflow WITH PASSWORD 'airflow';
        GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
    END IF;
END $$;

-- Создаем базу и пользователя для MLflow
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'mlflow') THEN
        CREATE DATABASE mlflow;
        CREATE USER mlflow WITH PASSWORD 'mlflow';
        GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;
    END IF;
END $$;

-- Создаем базу и пользователя для Superset
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'superset') THEN
        CREATE DATABASE superset;
        CREATE USER superset WITH PASSWORD 'superset';
        GRANT ALL PRIVILEGES ON DATABASE superset TO superset;
    END IF;
END $$;

