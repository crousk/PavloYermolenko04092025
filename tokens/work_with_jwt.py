from time import sleep

import jwt
import datetime

JWT_SECRET = 'k-jhhgfghbjdfgdfhvbcfghkbjhfg'

payload = {
    "sub": "4545",
    'user_name': "Vasyl",
    "age": 18,
    "iat": datetime.datetime.now(datetime.timezone.utc),
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=5)
}

encode_jwt = jwt.encode(payload=payload, key=JWT_SECRET, algorithm='HS256')
print(encode_jwt)
sleep(6)

decode = jwt.decode(
    jwt=encode_jwt,
    key=JWT_SECRET,
    algorithms=['HS256'],
    # options={'verify_signature': False}
)
print(decode)