FROM python:3.9-slim 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY first_docker.py .

EXPOSE 8000

CMD ["uvicorn", "first_docker:app", "--host", "0.0.0.0", "--port", "8000"]

