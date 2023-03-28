from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "ee8b93f88b000896451907e0f6e7fe7b1fc62b096a3ff9b8166577eb9390150b"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
