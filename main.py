from fastapi import FastAPI, Header, HTTPException
from fastapi import Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt
import jwt
print(jwt.__file__)
import datetime
import logging
from textblob import TextBlob
import spacy
from googletrans import Translator
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Configurações do JWT
SECRET_KEY = "chave_secreta"
ALGORITHM = "HS256"

# Banco de dados fictício
usuarios_db = {
    "admin": "1234"
}

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# 🛑🛑 Adicionando CORS para permitir o frontend acessar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem (pode restringir depois)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os headers
)

# Carregue o modelo spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Inicialize o tradutor
translator = Translator()

# Configuração do Chatbot
chatbot = ChatBot("MeuChatbot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")  # Treina o chatbot com dados em português


class LoginRequest(BaseModel):
    username: str
    password: str

    # Modelo para receber o texto
class TextoRequest(BaseModel):
    texto: str

# Função para classificar texto
def classificar_texto(texto: str):
    # Exemplo simples de classificação
    if "bom" in texto or "excelente" in texto:
        return "positivo"
    elif "ruim" in texto or "péssimo" in texto:
        return "negativo"
    else:
        return "neutro"
    
    # Função para analisar sentimento usando TextBlob
def analisar_sentimento(texto: str):
    blob = TextBlob(texto)
    # Retorna o polaridade para indicar se é positivo ou negativo
    if blob.sentiment.polarity > 0:
        return "positivo"
    elif blob.sentiment.polarity < 0:
        return "negativo"
    else:
        return "neutro"

@app.post("/v1/login")
def login(request: LoginRequest):
    if request.username in usuarios_db and usuarios_db[request.username] == request.password:
        token = jwt.encode(
            {"sub": request.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        logger.info(f"Login bem-sucedido para o usuário {request.username}.")
        return {"access_token": token}
    
    logger.warning(f"Tentativa de login falha para o usuário {request.username}.")
    raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

@app.get("/v1/endpoint_protegido")
def endpoint_protegido(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extrai o token do formato 'Bearer TOKEN'
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Acesso autorizado!"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


# Endpoint para classificar texto
@app.post("/v1/classificar_texto")
def classificar_texto_endpoint(request: TextoRequest):
    try:
        classificacao = classificar_texto(request.texto)
        logger.info(f"Texto classificado: {classificacao}")
        return {"classificacao": classificacao}
    except Exception as e:
        logger.error(f"Erro na classificação do texto: {e}")
        raise HTTPException(status_code=500, detail="Erro na classificação do texto")
        
@app.post("/v1/analisar_sentimento")
def analisar_sentimento_endpoint(request: TextoRequest):
    try:
        blob = TextBlob(request.texto)
        return {
            "sentimento": {
                "polaridade": blob.sentiment.polarity,
                "subjetividade": blob.sentiment.subjectivity
            }
        }
    except Exception as e:
        logger.error(f"Erro na análise de sentimento: {e}")
        raise HTTPException(status_code=500, detail="Erro na análise de sentimento")

@app.post("/v1/analisar_entidades")
def analisar_entidades_endpoint(request: TextoRequest):
    try:
        doc = nlp(request.texto)
        entidades = [{"texto": ent.text, "tipo": ent.label_} for ent in doc.ents]
        return {"entidades": entidades}
    except Exception as e:
        logger.error(f"Erro na análise de entidades: {e}")
        raise HTTPException(status_code=500, detail="Erro na análise de entidades")

@app.post("/v1/traduzir")
def traduzir_endpoint(request: TextoRequest, destino: str = "en"):
    try:
        traducao = translator.translate(request.texto, dest=destino)
        return {
            "texto_original": request.texto,
            "texto_traduzido": traducao.text,
            "idioma_original": traducao.src,
            "idioma_destino": traducao.dest
        }
    except Exception as e:
        logger.error(f"Erro na tradução: {e}")
        raise HTTPException(status_code=500, detail="Erro na tradução")

@app.post("/v1/chatbot")
def chatbot_endpoint(request: TextoRequest):
    try:
        resposta = chatbot.get_response(request.texto)
        return {"resposta": str(resposta)}
    except Exception as e:
        logger.error(f"Erro no chatbot: {e}")
        raise HTTPException(status_code=500, detail="Erro no chatbot")
