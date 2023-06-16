FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8050



RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

