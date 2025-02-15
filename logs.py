from loguru import logger

logger.add("logs/api.log", rotation="1 day", level="INFO")

def log_requisicao(endpoint, dados):
    logger.info(f"Requisição para {endpoint}: {dados}")
