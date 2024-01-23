# Calc API
This is an API for a simple calculator.

## Setup
```
pipenv shell
cd src
pip install -r requirements.txt
```

## Build container
```
docker build -t <DEINOIMAGENAME> .
```

## Run container
```
docker run -dp 8000:5000 -e API_PORT=5000 <DEINOIMAGENAME>
```

```
-dp = detached, port forwarding
-e = ENV vars
```