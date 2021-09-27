FROM python:3.8.8-slim 

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./src/main.py /app/main.py
COPY ./src/app /app/app

RUN apt-get update \
    && apt-get -y dist-upgrade \
    && pip install -r /app/requirements.txt \
    && rm -rf /var/lib/apt/lists/* /var/cache/*

EXPOSE 8080
CMD ["python3", "main.py"]

