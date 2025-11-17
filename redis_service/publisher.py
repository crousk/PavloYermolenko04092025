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

while True:
    msg = input("Введи повідомлення для school: ")
    client.publish("school", msg)