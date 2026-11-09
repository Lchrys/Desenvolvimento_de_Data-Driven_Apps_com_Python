*README elaborado com ajuda da IA Grok 4.6 e revisado pelo autor do projeto.*

# Parte 1 — Questão 2: tradução inglês-francês

API FastAPI que recebe um texto em inglês e traduz para o francês com o modelo 'Helsinki-NLP/opus-mt-en-fr' da Hugging Face.

Textos longos são separados por ponto final, traduzidos frase a frase e reunidos na resposta.

## Como executar

Na pasta 'parte1_q2_traducao_en_fr', crie e ative um ambiente virtual, instale as dependências e inicie o servidor:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Na primeira execução, o modelo de tradução é baixado automaticamente. Com o servidor em execução, acesse:

- http://127.0.0.1:8000/docs — documentação interativa (Swagger UI)
- http://127.0.0.1:8000/redoc — documentação alternativa (ReDoc)

Em outro terminal, com o ambiente ativado:

```
python test.py
```

## Organização do projeto

- 'main.py': cria a instância FastAPI e registra as rotas.
- 'routers/translation_routers.py': define o endpoint POST '/translate'.
- 'services/translation_services.py': carrega o pipeline de tradução e processa frases curtas e textos mais longos.
- 'models/translation_models.py': modelos Pydantic de entrada e de resposta.
- 'test.py': exemplo de requisição HTTP com 'requests'.
- 'requirements.txt': bibliotecas necessárias.

## Rotas

- POST '/translate': recebe um texto em inglês e retorna a tradução em francês.

Exemplo de corpo JSON:

```json
{
  "text": "Hello, how are you? I hope you have a good day."
}
```

Exemplo de resposta:

```json
{
  "original_text": "Hello, how are you? I hope you have a good day.",
  "translated_text": "Bonjour, comment allez-vous? J'espère que vous passez une bonne journée."
}
```
