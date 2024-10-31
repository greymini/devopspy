from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from model import User,Gender, Role


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Ayush", 
        last_name="Singh",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id=uuid4(),
        first_name = "Aditya",
        last_name = "Ratnaparkhi",
        gender = Gender.male,
        roles = [Role.admin]
    ),
    User(
        id=uuid4(),
        first_name = "Ankita",
        last_name = "Rathod",
        gender = Gender.female,
        roles = [Role.user]
    )

]


@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exist"
    )