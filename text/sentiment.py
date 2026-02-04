from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="blanchefort/rubert-base-cased-sentiment"
)

text = "Мне очень понравилось это мероприятие"

result = classifier(text)

print(result)

# Цель:
# анализ тональности текстовых сообщений

# Выход:
# метка тональности и значение уверенности модели

# python text/sentiment.py

# python audio/audio_classification.py

# python image/image_classification.py

# python video/video_detection.py

# python llm/llm_demo.py

