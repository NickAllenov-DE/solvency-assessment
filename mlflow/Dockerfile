FROM python:3.11-slim

WORKDIR /app

# Устанавливаем утилиты и очищаем кеш APT
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Копируем скрипт запуска
COPY entrypoint.sh . 
RUN chmod +x entrypoint.sh

# Указываем команду запуска
CMD ["/bin/bash", "/app/entrypoint.sh"]
