# fastapi-frontend


# Projeto FastAPI 

Este projeto é uma API desenvolvida em **FastAPI** para a disciplina Construção de APIs para Inteligência Artificial da Pós-Graduação em Sistemas e Agentes Inteligentes - UFG,  que oferece funcionalidades de atendimento automatizado utilizando técnicas de processamento de linguagem natural (NLP). Ele inclui endpoints para classificação de texto, análise de sentimento, tradução de texto e interação com um chatbot.

## Funcionalidades

- **Login e Autenticação**: Autenticação de usuários com JWT (JSON Web Tokens).
- **Classificação de Texto**: Classifica textos em categorias predefinidas.
- **Análise de Sentimento**: Analisa o sentimento de um texto (positivo, negativo ou neutro).
- **Tradução de Texto**: Traduz textos para diferentes idiomas.
- **Chatbot**: Interage com um chatbot treinado em português.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção de APIs em Python.
- **JWT**: Autenticação baseada em tokens.
- **spaCy**: Processamento de linguagem natural.
- **TextBlob**: Análise de sentimento.
- **ChatterBot**: Chatbot com suporte a treinamento em português.
- **Googletrans**: Tradução de textos.

## Como Configurar o Projeto

### Pré-requisitos

- Python 3.8 ou superior.
- Git (opcional, para clonar o repositório).

### Passos para Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Dane82/fastapi-frontend.git
   cd fastapi-frontend

    Crie um ambiente virtual:
    
    python -m venv venv

    Ative o ambiente virtual:

        No Windows:     
        venv\Scripts\activate

        No Linux/Mac:
        source venv/bin/activate

    Instale as dependências:
    pip install -r requirements.txt

    Execute o projeto:
    uvicorn main:app --reload

    Acesse a API:

        Acesse o Swagger UI em: http://localhost:8000/docs.

Como Usar a API
Endpoints Disponíveis

    POST /v1/login: Faz login e retorna um token JWT.

    GET /v1/endpoint_protegido: Endpoint protegido que requer autenticação.

    POST /v1/classificar_texto: Classifica um texto em categorias predefinidas.

    POST /v1/analisar_sentimento: Analisa o sentimento de um texto.

    POST /v1/traduzir: Traduz um texto para o idioma especificado.

    POST /v1/chatbot: Interage com o chatbot.


Como Contribuir

    Faça um fork do repositório.

    Crie uma branch para sua feature:
 
    git checkout -b minha-feature

    Faça commit das suas alterações:
    
    git commit -m "Adiciona nova funcionalidade"

    Envie as alterações:
    
    git push origin minha-feature

    Abra um pull request no repositório original.

Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
Contato

Se tiver dúvidas ou sugestões, entre em contato:

  

    GitHub: Dane82
