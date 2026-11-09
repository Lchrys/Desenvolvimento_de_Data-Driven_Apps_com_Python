*README elaborado com ajuda da IA Grok 4.6 e revisado pelo autor do projeto.*

# Parte 1 — Questão 1: geração de texto com GPT-2

API FastAPI que recebe uma frase em JSON e usa o modelo GPT-2 da Hugging Face para gerar uma continuação de texto.

## Como executar

Na pasta 'parte1_q1_gpt2', crie e ative um ambiente virtual, instale as dependências e inicie o servidor:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Na primeira execução, o modelo GPT-2 é baixado automaticamente. Com o servidor em execução, acesse:

- http://127.0.0.1:8000/docs — documentação interativa (Swagger UI)
- http://127.0.0.1:8000/redoc — documentação alternativa (ReDoc)

Em outro terminal, com o ambiente ativado:

```
python test.py
```

## Organização do projeto

- 'main.py': cria a instância FastAPI e registra as rotas.
- 'routers/generation_routers.py': define o endpoint POST '/generate'.
- 'services/generation_services.py': carrega o pipeline 'text-generation' com o modelo 'gpt2' e gera o texto.
- 'models/generation_models.py': modelos Pydantic de entrada e de resposta.
- 'test.py': exemplo de requisição HTTP com 'requests'.
- 'requirements.txt': bibliotecas necessárias.

## Rotas

- POST '/generate': recebe uma frase e retorna a continuação gerada pelo GPT-2.

Exemplo de corpo JSON:

```json
{
  "text": "Once upon a time"
}
```

Exemplo de resposta:

```json
{
  "input": "Once upon a time",
  "generated_text": " there was a small village..."
}
```
