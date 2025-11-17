import redis
import os
from dotenv import load_dotenv

load_dotenv()

client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

pubsub = client.pubsub()
pubsub.subscribe("school")

with open("messages.txt", "a", encoding="utf-8") as file:
    print("Слухаю канал 'school'...")

    for message in pubsub.listen():
        if message["type"] == "message":
            text = message["data"]
            print("Отримано:", text)
            if "Контрольна робота" in text.lower():
                file.write(text + "\n")