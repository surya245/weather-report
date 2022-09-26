FROM python:3.10-alpine
WORKDIR /app
ENV FLASK_APP=/app/src/server.py
ENV FLASK_DEBUG=1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


