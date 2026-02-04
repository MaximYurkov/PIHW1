from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="blanchefort/rubert-base-cased-sentiment"
)

text = "Мне очень понравилось это мероприятие"

result = classifier(text)

print(result)
