import datetime
import time
import jwt

SECRET_KEY = "my_secret_key"

payload = {
    "name": "Павло",
    "age": 20,
    "city": "Київ",
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=10)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Token created:", token)

time.sleep(15)

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
print(decoded)