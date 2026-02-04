import requests

r = requests.post(
    "http://localhost:11434/api/pull",
    json={"name": "llama3.2:3b"}
)

print(r.text)
