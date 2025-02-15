from pydantic import BaseModel

class SentimentoRequest(BaseModel):
    mensagem: str

class RespostaRequest(BaseModel):
    pergunta: str

class Usuario(BaseModel):
    username: str
    password: str
