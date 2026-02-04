import requests

r = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "gemma3:4b",
        "messages": [
            {"role": "user", "content": "Коротко объясни, что такое сумма в алгебре."}
        ],
        "stream": False
    }
)

print(r.json()["message"]["content"])

