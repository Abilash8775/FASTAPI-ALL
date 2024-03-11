from passlib.context import CryptContext
pxd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")
class Hash():
    def bcrypt(password:str):
        return pxd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return pxd_cxt.verify(plain_password,hashed_password)