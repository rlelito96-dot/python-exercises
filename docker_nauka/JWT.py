

from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os
import jwt


load_dotenv()

JWT_SECRET= os.getenv("JWT_SECRET")
JWT_ALGORITHM= os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES= int(os.getenv("JWT_EXPIRE_MINUTES"))


def issue_jwt(user_id: int, role: str) -> str:
    header= {
        "alg": JWT_ALGORITHM,
        "typ": "JWT"

    }

    payload = {
        "user_role": role,
        "user_id": user_id,
        "exp": int((datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRE_MINUTES)).timestamp())

    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM, headers=header)
    return token

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

token = issue_jwt(1, "user")
print(token)
print(verify_jwt(token))








