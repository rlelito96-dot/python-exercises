# fastapi_docker_training.py

from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

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

# ----- App -----
app = FastAPI(title="Docker Training API")

@app.get("/")
def root():
    return {"message": "Docker + FastAPI training project"}

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