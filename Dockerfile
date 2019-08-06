FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install -y libzbar0
RUN pip install --trusted-host pypi.python.org -r requirements/base.txt

ENV PYTHONPATH /app

CMD ["python", "qr_bot/start_bot.py"]
