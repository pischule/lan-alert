FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y iputils-ping
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]