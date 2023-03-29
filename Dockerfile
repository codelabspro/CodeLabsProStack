FROM python:3.10

RUN mkdir -p /code
WORKDIR /code

COPY ./app/requirements.txt /code/app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/app/requirements.txt

COPY ./app /code/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

