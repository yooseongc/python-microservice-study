import os
import jwt


with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "pubkey.pem") as f:
    PUBKEY = f.read()
    

with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "privkey.pem") as f:
    PRIVKEY = f.read()
    
    
def create_token(**data):
    return jwt.encode(data, PRIVKEY, algorithm="RS512")


def read_token(token):
    return jwt.decode(token, PUBKEY, algorithms=["RS512"])


token = create_token(some="data", inthe="token")
print(token)
read = read_token(token)
print(read)
