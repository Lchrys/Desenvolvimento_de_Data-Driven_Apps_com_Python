from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")


class TextGenerator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        result = pipe(
            self.text,
            max_new_tokens=50,
            return_full_text=False,
            pad_token_id=pipe.tokenizer.eos_token_id,
        )
        self.response = result[0]["generated_text"]
        return self.response
