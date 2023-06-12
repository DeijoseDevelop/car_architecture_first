# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Time Zone
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
# RUN useradd -m admin
# USER admin

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && \
    apt-get install -y python3-pip

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

# collect static files
# RUN python manage.py collectstatic --noinput