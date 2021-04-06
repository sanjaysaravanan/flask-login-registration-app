FROM python:3.7.0-alpine3.8
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY src /app/src
RUN pip install -r requirements.txt
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 8000
CMD flask run
