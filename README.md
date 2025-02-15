# fastapi-frontend


# Projeto FastAPI 

Este projeto é uma API desenvolvida em **FastAPI** para a disciplina Construção de APIs para Inteligência Artificial da Pós-Graduação em Sistemas e Agentes Inteligentes - UFG,  que oferece funcionalidades de atendimento automatizado utilizando técnicas de processamento de linguagem natural (NLP). Ele inclui endpoints para classificação de texto, análise de sentimento, tradução de texto e interação com um chatbot.



### **1. Análise de Sentimento (TextBlob)**  
**O que faz?**  
É como um "detector de emoções" para textos. Ele lê uma frase e diz se o sentimento é **positivo**, **negativo** ou **neutro**.  

**Exemplo prático:**  
Se você escrever *"Adorei esse atendimento, foi incrível!"*, ele vai entender que é algo **positivo**.  
Se escrever *"Estou muito frustrado com o serviço"*, ele identifica como **negativo**.  

**Como funciona?**  
Ele analisa palavras-chave (como "adorar", "frustrado") e calcula uma "pontuação" de sentimento.  

---

### **2. Identificação de Entidades (spaCy)**  
**O que faz?**  
Age como um "detetive de informações", identificando elementos importantes em um texto:  
- **Pessoas** (ex: "Maria"),  
- **Lugares** (ex: "São Paulo"),  
- **Datas** (ex: "15 de agosto"),  
- **Organizações** (ex: "Google").  

**Exemplo prático:**  
Se você digitar *"Marco viajou para Paris na última sexta-feira"*, ele destaca:  
- **Pessoa:** Marco,  
- **Local:** Paris,  
- **Data:** sexta-feira.  

**Para que serve?**  
Útil para extrair dados automáticos de textos, como em relatórios ou formulários.  

---

### **3. Chatbot (ChatterBot)**  
**O que faz?**  
É um "atendente virtual" que conversa com as pessoas, respondendo perguntas de forma automática.  

**Exemplo prático:**  
Se você perguntar *"Como faço para cancelar minha conta?"*, ele busca respostas pré-programadas ou aprende com conversas passadas.  

**Como funciona?**  
Ele usa um banco de dados de perguntas e respostas, e quanto mais interage, mais "esperto" fica (como um aluno que estuda para provas).  

---

### **4. Tradutor Automático (Googletrans)**  
**O que faz?**  
Funciona como um "tradutor instantâneo", convertendo textos de um idioma para outro (ex: português ➔ inglês).  

**Exemplo prático:**  
Se você escrever *"Bom dia!"*, ele pode traduzir para *"Good morning!"* em inglês ou *"¡Buenos días!"* em espanhol.  

**Para que serve?**  
Útil para aplicações que precisam atender pessoas de diferentes países.  

---

### **Resumo das IAs no Projeto**  
- **Análise de Sentimento:** Entende emoções em textos.  
- **Identificação de Entidades:** Encontra informações-chave.  
- **Chatbot:** Conversa automática com usuários.  
- **Tradutor:** Quebra barreiras de idiomas.  

Todas trabalham juntas para criar um sistema de atendimento mais inteligente e útil! 😊  

---

### **Analogia Final**  
Imagine que seu projeto é uma **equipe de especialistas**:  
- O **detetive de emoções** (TextBlob) analisa o humor das mensagens.  
- O **detetive de informações** (spaCy) coleta dados importantes.  
- O **atendente** (ChatterBot) responde perguntas.  
- O **tradutor** (Googletrans) ajuda a comunicar em outros idiomas.  

Juntos, eles fazem o atendimento ser mais rápido, preciso e humano (mesmo sendo automatizado!).


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
