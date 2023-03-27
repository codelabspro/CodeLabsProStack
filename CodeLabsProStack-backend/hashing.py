from passlib.context import CryptContext

pwdCtx = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password: str):
        hashedPassword = pwdCtx.hash(password)
        return hashedPassword

    def verify(plain_password, hashed_password):
        return pwdCtx.verify(plain_password, hashed_password)
