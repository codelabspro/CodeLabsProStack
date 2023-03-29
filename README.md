# CodeLabsProStack

CodeLabsProStack is a SvelteKit - NextJS - (fast)API - Postgres- stack toolkit for building, testing and deploying fullstack CMS, CRM and Mobile SaaS applications

## Useful Links

https://codeverter.vercel.app

## Screenshots

## Steps for blog

```

==> python3 -m venv myvenv

==> source myvenv/bin/activate

pip install fastapi

pip install "uvicorn[standard]"

pip install pydantic

pip install --upgrade pip

==> python --version (should be 3.9 or higher)
Python 3.10.9

==> uvicorn --version
Running uvicorn 0.15.0 with CPython 3.10.9 on Darwin

pip install sqlalchemy

pip install passlib

pip install bcrypt

pip install sqladmin

```
## JWT Dependencies

```
pip install "python-jose[cryptography]"

pip install "passlib[bcrypt]"

```

## Run backend locally

```
cd src

python3 -m venv myvenv OR source myvenv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload

```


## Deployment

* Dockerfile https://fastapi.tiangolo.com/deployment/docker/

```
Dockerfile¶

Now in the same project directory create a file Dockerfile with:

#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

```

* Build Dockerfile

```
docker build -t codelabsprostack:0.0.1 .
```

* Run Docker Container Locally

```
docker run -p 8080:8080 --name codelabsprostack codelabsprostack:0.0.1
```

* List docker images

```
docker images -a
```


* List running docker processes

```
docker ps -a
```

* Remove running docker process

```
docker rm codelabsprostack
```
