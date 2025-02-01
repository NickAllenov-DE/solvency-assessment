-- Создаем базу данных, если её нет
SELECT 'CREATE DATABASE airflow'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'airflow')\gexec

SELECT 'CREATE DATABASE mlflow'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mlflow')\gexec

SELECT 'CREATE DATABASE superset'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'superset')\gexec

-- Создаем пользователей, если их нет
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'airflow') THEN
        CREATE USER airflow WITH PASSWORD 'airflow';
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'mlflow') THEN
        CREATE USER mlflow WITH PASSWORD 'mlflow';
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'superset') THEN
        CREATE USER superset WITH PASSWORD 'superset';
    END IF;
END $$;

-- Даем права на базы данных
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;
GRANT ALL PRIVILEGES ON DATABASE superset TO superset;

-- Даем полные права на схему public для каждого пользователя
\c mlflow
GRANT USAGE, CREATE ON SCHEMA public TO mlflow;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO mlflow;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO mlflow;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO mlflow;

\c airflow
GRANT USAGE, CREATE ON SCHEMA public TO airflow;

\c superset
GRANT USAGE, CREATE ON SCHEMA public TO superset;
