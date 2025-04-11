# core/bot.py
from transformers import pipeline

from transformers import pipeline


class QuestionAnsweringBot2:
    _instance = None
    _generator = None

    def __new__(cls, model_name="gpt2"):
        if cls._instance is None:
            print("🔄 Загружается GPT-2...")
            cls._instance = super(QuestionAnsweringBot2, cls).__new__(cls)
            cls._generator = pipeline("text-generation", model=model_name)
            print("✅ GPT-2 загружен.")
        return cls._instance

    def ask(self, question: str) -> str:
        # Формируем промпт
        prompt = f"Вопрос: {question}\nОтвет:"

        result = self._generator(
            prompt,
            max_length=150,  # увеличь до 200–300 при необходимости
            num_return_sequences=1,
            do_sample=True,  # чтобы не повторял одно и то же
            top_p=0.95,
            temperature=0.8  # регулирует креативность
        )

        return result[0]['generated_text'][len(prompt):].strip()


class QuestionAnsweringBot:
    _instance = None
    _qa_pipeline = None

    def __new__(cls, model_name="deepset/roberta-base-squad2"):
        if cls._instance is None:
            print("🔄 Загружается модель...")
            cls._instance = super(QuestionAnsweringBot, cls).__new__(cls)
            cls._qa_pipeline = pipeline("question-answering", model=model_name)
            print("✅ Модель загружена.")
        return cls._instance

    def ask(self, question: str, context: str) -> str:
        result = self._qa_pipeline(question=question, context=context)
        return result['answer']
