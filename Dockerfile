FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV ENV=production

EXPOSE 5000

CMD ["python", "app.py"]