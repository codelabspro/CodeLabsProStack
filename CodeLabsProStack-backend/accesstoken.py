from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "ee8b93f88b000896451907e0f6e7fe7b1fc62b096a3ff9b8166577eb9390150b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
