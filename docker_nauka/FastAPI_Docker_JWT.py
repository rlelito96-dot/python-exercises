# Imports

from fastapi import FastAPI, HTTPException, status, Path, Depends, Header
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os
import jwt

# Load .env

load_dotenv()

JWT_SECRET= os.getenv("JWT_SECRET")
JWT_ALGORITHM= os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES= int(os.getenv("JWT_EXPIRE_MINUTES"))


# ----- Schemas -----
class User(BaseModel):
    name: str
    website: str
    age: int
    role: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None

# ----- Data -----
users = {
    1: {
        "name": "Josh",
        "website": "www.zerotoknowing.com",
        "age": 28,
        "role": "developer"
    }
}

# JWT Functions

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

def verify_jwt(token: str):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# Dependency
def get_current_user(authorization: str = Header(...)):
    # Authorization: "Bearer <token>"
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    return verify_jwt(token)

# ----- App -----
app = FastAPI(title="Docker Training API")

@app.get("/")
def root():
    return {"message": "Docker + FastAPI training project"}

# JWT Protected route example
@app.get("/users/me")
def get_me(token: str = Depends(get_current_user)):
    return {"message": "This is a protected endpoint", "user":token}


# User routes
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(gt=0)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = user.dict()
    return users[user_id]

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user = users[user_id]
    for field, value in user.dict(exclude_unset=True).items():
        stored_user[field] = value

    return stored_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users.pop(user_id)

# ----- Run (tylko jeśli uruchamiasz bez Dockera) -----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("first_docker:app", host="0.0.0.0", port=8000, reload=True)