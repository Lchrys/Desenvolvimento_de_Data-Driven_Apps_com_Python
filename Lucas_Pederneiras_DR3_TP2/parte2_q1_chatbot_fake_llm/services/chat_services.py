from langchain_community.llms import FakeListLLM

RESPONSES = {
    "olá": "Olá! Como posso ajudar?",
    "qual é o seu nome?": "Sou um chatbot de teste com Fake LLM.",
    "em qual continente fica o brasil?": "América do Sul",
    "como você funciona?": "Eu simulo respostas prontas para testar o fluxo da aplicação.",
}


class Chatbot:
    def __init__(self, message):
        self.message = message
        self.response = ""

    def run(self):
        key = self.message.strip().lower()
        answer = RESPONSES.get(
            key,
            "Desculpe, não posso responder essa pergunta no momento.",
        )
        llm = FakeListLLM(responses=[answer])
        self.response = llm.invoke(self.message)
        return self.response
