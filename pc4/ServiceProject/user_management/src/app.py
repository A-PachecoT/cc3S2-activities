from fastapi import FastAPI, HTTPException
from src.models.user import User
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

app = FastAPI()
user_repository = UserRepository()
user_service = UserService(user_repository)

@app.post("/users/", response_model=User)
async def create_user(user: User):
    return user_service.create_user(user)

@app.get("/users/", response_model=list[User])
async def get_users():
    return user_service.get_all_users()

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    return user

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    updated_user = user_service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    return updated_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    return {"message": "Usuario eliminado exitosamente"}