from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Endpoints")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

# @app.get("/user")
# def getUser():
#     return{
#         "message": "Endpoint created successfuly"
#     }

# ractice Problem: User Retrieval API

user_db =[
  {"id": 1, "name": "Alice", "email": "alice@example.com"},
  {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.get("/user")
def getUser():
    userData = user_db
    return userData

@app.get("/userDetails/{user_id}")
def user_details(user_id: int):
    userData = user_db
    for data in userData:
       if data["id"] == user_id:
            return data
    raise HTTPException(status_code= 404, details="Kindly add the valid student")


# Improve endpoints for the fast api
@app.get("/users")
def get_users() -> list[dict]:
    return user_db


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    for user in user_db:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

class newStudent(BaseModel):
    name: str
    email: str

 # creating the post endpoint using the fastapi post endpoint 
@app.post("/student_create")
def studentCreate(newStudent):
    new_user = {
        "id": max(existing_user["id"] for existing_user in user_db) + 1,
        "name": user.name,
        "email": user.email,
    }
    user_db.append(new_user)
    print(new_user)
    return new_user
