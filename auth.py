import jwt
import datetime
from fastapi import HTTPException, Depends, Header
from app.models import Usuario

SECRET_KEY = "chave_secreta"
ALGORITHM = "HS256"
usuarios_db = {"admin": "1234"}

def autenticar_usuario(username: str, password: str):
    if username in usuarios_db and usuarios_db[username] == password:
        token = jwt.encode(
            {"sub": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

def obter_usuario_logado(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")
    
    token = authorization.split(" ")[1]
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"username": payload["sub"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
