FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY food_back/ .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "food_back.wsgi"]

