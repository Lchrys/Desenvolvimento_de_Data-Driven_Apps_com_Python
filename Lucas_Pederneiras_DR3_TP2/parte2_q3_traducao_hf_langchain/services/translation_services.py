from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
llm = HuggingFacePipeline(pipeline=pipe)
prompt = PromptTemplate.from_template("{text}")
chain = prompt | llm


class Translator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        self.response = chain.invoke({"text": self.text})
        return self.response
