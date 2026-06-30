from fastapi import FastAPI
from routers import users

app = FastAPI(title="My App with PostgreSQL")

app.include_router(users.router)