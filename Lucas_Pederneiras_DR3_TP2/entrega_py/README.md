*README gerado pela IA Claude Sonnet 5.5 (Anthropic) e revisado pelo autor do projeto.*

# TP2: Aplicações FastAPI e LangChain

Cinco aplicações, uma por arquivo. Cada arquivo reúne, em seções, os modelos Pydantic (`models`), a lógica (`services`), as rotas (`routers`) e a instância `app` do FastAPI.

| Arquivo | Questão | Rota | Corpo da requisição (JSON) |
|---|---|---|---|
| `p1q1.py` | Parte 1, Q1: geração de texto com GPT-2 | `POST /generate` | `{"text": "Once upon a time"}` |
| `p1q2.py` | Parte 1, Q2: tradução en→fr (`Helsinki-NLP/opus-mt-en-fr`) | `POST /translate` | `{"text": "Hello, how are you?"}` |
| `p2q1.py` | Parte 2, Q1: chatbot com Fake LLM (LangChain) | `POST /chat` | `{"message": "Em qual continente fica o Brasil?"}` |
| `p2q2.py` | Parte 2, Q2: tradução en→fr com OpenAI via LangChain | `POST /translate` | `{"text": "Hello, how are you?"}` |
| `p2q3.py` | Parte 2, Q3: tradução en→de (`Helsinki-NLP/opus-mt-en-de`) com LangChain | `POST /translate` | `{"text": "Hello, how are you?"}` |

## Requisitos

- Python 3.12 ou 3.13 (testado com 3.13; com o Python 3.15 a instalação de uma dependência do LangChain falhou).
- Conexão com a internet na primeira execução de `p1q1`, `p1q2` e `p2q3`, que baixam os modelos da Hugging Face.
- Uma chave da OpenAI, somente para o `p2q2`.

## Instalação

Nesta pasta (`entrega_py`):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Chave da OpenAI (somente `p2q2`)

```
copy .env.example .env
```

Edite o `.env` e preencha a linha `OPENAI_API_KEY=` com a sua chave. O arquivo `.env` não deve ser enviado ao GitHub nem incluído no zip. Sem a chave, o `p2q2` não inicia.

## Executar

Suba um aplicativo por vez (todos usam a porta 8000), trocando `p1q1` pelo arquivo desejado:

```
python -m uvicorn p1q1:app --reload
```

Com o servidor em execução, a documentação interativa (Swagger) fica em http://127.0.0.1:8000/docs e permite enviar o JSON da tabela acima.

Para enviar uma requisição pelo terminal, em outra janela, com o ambiente ativado:

```
python -c "import requests; print(requests.post('http://127.0.0.1:8000/generate', json={'text': 'Once upon a time'}).json())"
```

Troque a rota e o JSON conforme a tabela (por exemplo, `/translate` com `{'text': 'Hello, how are you?'}`, ou `/chat` com `{'message': 'Olá'}`).

## Observações

- `p1q1`: o GPT-2 gera no máximo 50 tokens novos por chamada; a continuação varia a cada execução.
- `p1q2`: textos com mais de uma frase são separados por pontuação final (`.`, `!`, `?`) e cada frase é traduzida separadamente.
- `p2q1`: não precisa de chave nem de modelo; responde com uma lista pré-definida e, fora dela, com uma mensagem padrão.
- `p2q2`: usa o modelo `gpt-4o-mini` diretamente na OpenAI (sem Groq); se a chamada falhar, a API responde HTTP 502.
- `p2q3`: o LangChain encapsula o pipeline da `transformers`; o pipeline é criado com a task `translation`.
