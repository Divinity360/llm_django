# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "yourproject.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
