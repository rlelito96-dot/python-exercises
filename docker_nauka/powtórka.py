# Imports
from fastapi import FastAPI, Header, Depends, status, Path, HTTPException, Body
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from typing import Optional
import os
import jwt

# Load .env
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES"))
JWT_ISSUER = os.getenv("JWT_ISSUER")

# Passlib
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Validation
if not JWT_SECRET or not JWT_ALGORITHM or not JWT_EXPIRE_MINUTES:
    raise RuntimeError("Invalid environment")

# Schemas
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

class RegisterUser(BaseModel):
    name: str
    website: str
    age: int
    role: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Data
users = {
    1:{
    "name": "Rafal",
    "website": "www.rlelito96.com",
    "age": 24,
    "role": "developer",
    "password_hash": pwd_context.hash("nofear123")

    }
}

# JWT functions
async def issue_jwt(user_id: int, role: str) -> str:
    header = {
        "alg": JWT_ALGORITHM,
        "typ": "JWT"
    }

    payload = {
        "user_id": user_id,
        "role": role,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRE_MINUTES)).timestamp()),
        "iss": JWT_ISSUER
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM, headers=header)

    return token

async def verify_jwt(token):

    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        if decoded.get("iss") != JWT_ISSUER:
            raise HTTPException(status_code=401, detail="Invalid token")

        return decoded

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Dependency Authorization
async def get_current_user(authorization: str = Header(...)) -> dict:
    """Dependency that authenticates a user using a Bearer JWT token.

    This function extracts the JWT token from the Authorization header,
    verifies it using `verify_jwt`, and returns the decoded payload.
    """
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authorization")

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization")

    return await verify_jwt(token)

# Permissions
async def developer_or_admin(user: dict = Depends(get_current_user)) -> dict:
    """Allows access only to users with developer or admin role."""
    if user["role"] not in ["developer", "admin"]:
        raise HTTPException(status_code=403, detail="Forbidden")

    return user

# App
app = FastAPI(title="My app")

@app.get("/")
async def root():
    return {"message": "My app"}

# Login
@app.post("/login", response_model=Token)
async def login(user_id: int = Body(...), password: str = Body(...)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User no found")

    user = users[user_id]

    # Password verification
    if not pwd_context.verify(password, user["password_hash"]):
        raise HTTPException(status_code=403, detail="Invalid credentials")

    #Generating token
    token = await issue_jwt(user_id=user_id, role=user["role"])

    return Token (access_token= token, token_type="bearer")

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: RegisterUser ):
    new_id = max(users.keys()) + 1 if users else 1

    password_hash = pwd_context.hash(user.password)

    users[new_id] = {
        "name": user.name,
        "website": user.website,
        "age": user.age,
        "role": user.role,
        "password_hash": password_hash
    }

    return {"user_id": new_id, "name": user.name, "role": user.role}

# JWT Protected route example
@app.get("/users/get_me")
async def get_me(user: str = Depends(get_current_user)):
    return {"message": "This is a protected endpoint", "user": user}

# User routes
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(gt=0)) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User no found")

    user = users[user_id].copy()
    user.pop("password_hash")

    return user

@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
async def create_user(user_id: int, user: User) -> dict:
    if user_id in users:
        raise HTTPException(status_code=404, detail="User already exist")

    users[user_id] = user.dict()

    return users[user_id]

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UpdateUser) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User no found")

    stored_user = users[user_id]

    for field, value in user.dict(exclude_unset=True).items():
        stored_user[field] = value

    return stored_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, user: dict = Depends(developer_or_admin)):
    """Deletes a user. Requires developer or admin permissions."""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User no found")

    users.pop(user_id)

    return

# Run (only if u running without Docker)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("My_app:app", port=8000, host="0.0.0.0", reload=True)
