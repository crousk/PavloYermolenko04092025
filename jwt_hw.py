import jwt
import datetime


SECRET_KEY = "my_secret_key"

payload = {
    "name": "Павло",
    "age": 20,
    "city": "Київ",
    "exp": datetime.datetime.now() + datetime.timedelta(seconds=1000)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("generated:\n", token)

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print("decoded:\n", decoded)