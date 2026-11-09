import re

from transformers import pipeline

pipe = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")


class Translator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        sentences = [
            s.strip()
            for s in re.split(r"(?<=[.!?])\s+", self.text.strip())
            if s.strip()
        ]
        if len(sentences) <= 1:
            result = pipe(self.text)
            self.response = result[0]["translation_text"]
        else:
            results = pipe(sentences)
            translated = [item["translation_text"] for item in results]
            self.response = " ".join(translated)
        return self.response
