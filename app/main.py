from fastapi import FastAPI, HTTPException

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

@app.get("/user-details/{user_id}")
def userDetails(user_id: int):
    userData = user_db
    for data in user_db:
        data.id = user_id
        return data
raise HTTPException(status_code= 404, details="Kindly add the valid student")


