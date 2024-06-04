from jwt import encode, decode

KEY = 'my_secret_key'

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=KEY, algorithm='HS256')
    return token

def validate_token(token: str) -> dict:
    data = decode(jwt=token, key=KEY, verify=True, algorithms=['HS256'])
    return data
