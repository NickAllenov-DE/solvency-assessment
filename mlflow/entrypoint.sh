#!/bin/bash

# Ожидание доступности PostgreSQL
until nc -z -v -w30 postgres 5432; do
  echo "Ожидание PostgreSQL..."
  sleep 5
done
echo "PostgreSQL доступен."

# Ожидание MinIO
until curl --output /dev/null --silent --head --fail http://minio:9000/minio/health/live; do
  echo "Ожидание MinIO..."
  sleep 5
done
echo "MinIO доступен."

# Запуск MLflow
mlflow server \
    --backend-store-uri $MLFLOW_BACKEND_STORE_URI \
    --default-artifact-root $MLFLOW_ARTIFACT_ROOT \
    --host 0.0.0.0 --port 5000
