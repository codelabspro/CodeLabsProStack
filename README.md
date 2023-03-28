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

```

## Run backend

```
cd CodeLabsProStack-backend

python3 -m venv myvenv OR source myvenv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload

```
