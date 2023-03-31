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
###################################
uvicorn main:app --reload
###################################
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

## Frontend Develop
* Frontend (web) was created using SvelteKit with the below config

```

==> npm create skeleton-app@latest web
┌  Create Skeleton App (version 0.0.29)

Welcome to Skeleton 💀! A UI tookit for Svelte + Tailwind

Problems? Open an issue on https://github.com/skeletonlabs/skeleton/issues if none exists already.
│
◇  Add type checking with TypeScript?
│  Yes, using TypeScript syntax
│
◇  Add ESLint for code linting?
│  Yes
│
◇  Add Prettier for code formatting ?
│  Yes
│
◇  Add Playwright for browser testing ?
│  No
│
◇  Add Vitest for unit testing ?
│  No
│
◇  Install component dependencies:
│  CodeBlock (installs highlight.js), Popups (installs floating-ui)
│
◇  Pick tailwind plugins to add:
│  forms, typography, line-clamp
│
◇  Select a theme:
│  Crimson
│
◇  Which Skeleton app template?
│  Bare Bones
│
◇  Done installing

Done! You can now:

cd web

###################################
npm run dev
###################################
```



## Develop local

```
cd web

npm run dev

```

## Alembic

* Alembic for migrations

alembic init <alembic_folder_name>

```
pip install alembic

alembic init <alembic_migrations_folder> OR alembic init alembic

* alembic.ini
```
Add sqlalchemy.url = postgres://codelabsprostack_admin_1:@127.0.0.1/codelabsprostack_prod_1 to line 64 of alembic.ini
```


* script.py.mako
```
Add
import sqlmodel
below
import sqlalchemy as sa in script.py.mako
```

* env.py - In env.py
Below
from logging.config import fileConfig
```
from models import *
from sqlmodel import SQLModel
```

Change
```
target_metadata = None
```

to

```
target_metadata = SQLModel.metadata
```

* Alembic create migrations

```
cd app
alembic revision --autogenerate -m "Create"
alembic upgrade heads
```


## Useful Links

Alembic + SQLModel - https://www.youtube.com/watch?v=Rb4_90gG_Lc

Alembic - https://youtu.be/SdcH6IEi6nE

