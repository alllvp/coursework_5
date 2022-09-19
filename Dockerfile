FROM python:3.10

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

CMD gunicorn wsgi:app -b 0.0.0.0:8080