# Imagine de bază
FROM python:3.9-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierele necesare
COPY . /app/

# Instalăm pachetele
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul 8000
EXPOSE 8000

# Comanda de rulare a serverului Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
