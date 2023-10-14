FROM python:3.9

ARG DB_HOST
ARG DB_PORT
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_NAME=flask-demo
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]