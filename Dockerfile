FROM python:3.11-slim

RUN mkdir /app

COPY /src/requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt 

COPY src/main /app

EXPOSE 8000

WORKDIR /app

CMD ["python", "api.py"]