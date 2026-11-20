*README gerado pela IA Claude Sonnet 5.5 (Anthropic) e revisado pelo autor do projeto.*

# TP2: Desenvolvimento de Data-Driven Apps com Python

Aplicações simples com FastAPI, Hugging Face e LangChain, uma para cada questão prática do TP2.

As respostas teóricas, os diagramas e a tabela comparativa estão no PDF [Lucas_Pederneiras_DR3_TP2.pdf](Lucas_Pederneiras_DR3_TP2.pdf).

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| [entrega_py](entrega_py) | Versão da entrega: cinco arquivos (`p1q1.py`, `p1q2.py`, `p2q1.py`, `p2q2.py`, `p2q3.py`), um por questão, com `requirements.txt` e [README com as instruções de execução](entrega_py/README.md). |
| `parte1_q1_gpt2`, `parte1_q2_traducao_en_fr`, `parte2_q1_chatbot_fake_llm`, `parte2_q2_traducao_openai`, `parte2_q3_traducao_hf_langchain` | Mesmas aplicações organizadas em camadas (`routers/`, `services/`, `models/`), cada uma com `requirements.txt`, `test.py` e `README.md` próprio. |
| [diagramas](diagramas) | Diagramas de arquitetura das questões da Parte 2. |
| [prints](prints) | Prints dos testes das aplicações. |

## Questões e arquivos

| Questão | Arquivo da entrega | Versão em camadas |
|---|---|---|
| Parte 1, Q1: geração de texto com GPT-2 (`transformers`) | [p1q1.py](entrega_py/p1q1.py) | [parte1_q1_gpt2](parte1_q1_gpt2) |
| Parte 1, Q2: tradução en→fr com `Helsinki-NLP/opus-mt-en-fr` | [p1q2.py](entrega_py/p1q2.py) | [parte1_q2_traducao_en_fr](parte1_q2_traducao_en_fr) |
| Parte 2, Q1: chatbot com Fake LLM (LangChain) | [p2q1.py](entrega_py/p2q1.py) | [parte2_q1_chatbot_fake_llm](parte2_q1_chatbot_fake_llm) |
| Parte 2, Q2: tradução en→fr com OpenAI via LangChain | [p2q2.py](entrega_py/p2q2.py) | [parte2_q2_traducao_openai](parte2_q2_traducao_openai) |
| Parte 2, Q3: tradução en→de com `Helsinki-NLP/opus-mt-en-de` via LangChain | [p2q3.py](entrega_py/p2q3.py) | [parte2_q3_traducao_hf_langchain](parte2_q3_traducao_hf_langchain) |

As questões teóricas (Parte 1, Q3 e Q4; Parte 2, Q1 a Q6) estão respondidas no PDF.

## Como executar

- Versão da entrega: siga o [README da pasta entrega_py](entrega_py/README.md).
- Versão em camadas: siga o `README.md` dentro de cada pasta `parte*`.

A chave da OpenAI, necessária só para a Parte 2, Q2, fica em um arquivo `.env` local, que não é versionado. As pastas `entrega_py` e `parte2_q2_traducao_openai` trazem um `.env.example` como modelo.
