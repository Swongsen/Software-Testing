FROM python:3

RUN apt-get update
RUN pip install pytest

FROM mysql
EXPOSE 8080