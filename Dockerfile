FROM python:3.10

WORKDIR /app

COPY web-app /app/web-app

WORKDIR /app/web-app

RUN pip install -r requirements.txt

CMD ["python3", "./wsgi.py"]