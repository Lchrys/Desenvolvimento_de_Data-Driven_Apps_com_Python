import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = PromptTemplate.from_template(
    "Translate the following English text to French: {text}"
)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)
chain = prompt | llm | StrOutputParser()


class Translator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        self.response = chain.invoke({"text": self.text})
        return self.response
