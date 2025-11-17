import datetime
import jwt

SECRET_KEY = "my_secret_key"
WRONG_KEY = "wrong_secret"

payload = {
    "name": "Павло",
    "age": 20,
    "city": "Київ",
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=500)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Token created:", token)

decoded = jwt.decode(token, WRONG_KEY, algorithms=["HS256"])
print(decoded)