
# !pip install transformers

from transformers import pipeline

# Загружаем пайплайн для question-answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

context = """
Artificial Intelligence (AI) is a field of computer science focused on building smart machines capable of performing tasks that typically require human intelligence.
AI is being increasingly applied in education, helping both teachers and students with personalized learning, grading automation, and intelligent tutoring systems.
"""

# Вопрос от пользователя
question = "How does AI help in education?"

# Получение ответа
result = qa_pipeline(question=question, context=context)

print("❓ Question:", question)
print("📘 Context:", context)
print("✅ Answer:", result['answer'])


# pip install transformers
# pip install torch
# pip install huggingface_hub
# pip install hf_xet
# python -m pip install django-cors-headers