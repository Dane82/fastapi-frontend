from transformers import pipeline

# Modelo de sentimentos (pré-treinado)
sentimento_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analisar_sentimento(mensagem: str):
    resultado = sentimento_model(mensagem)[0]
    sentimento = "positivo" if resultado["label"] in ["4 stars", "5 stars"] else "negativo" if resultado["label"] in ["1 star", "2 stars"] else "neutro"
    return {"sentimento": sentimento, "confianca": resultado["score"]}

# Simulando LLM (pode ser substituído por OpenAI)
def gerar_resposta(pergunta: str):
    respostas = {
        "cancelar assinatura": "Acesse sua conta e vá até 'Configurações' > 'Assinatura' > 'Cancelar'.",
        "horário de atendimento": "Nosso atendimento funciona das 8h às 18h de segunda a sexta."
    }
    return {"resposta": respostas.get(pergunta.lower(), "Desculpe, não tenho essa informação.")}

