from fastapi import FastAPI
from src.routes.user_routes import configure_routes
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

app = FastAPI(
    title="Gestión de Usuarios API",
    description="API para gestión de usuarios",
    version="1.0.0"
)

# Configuración de dependencias
user_repository = UserRepository()
user_service = UserService(user_repository)

# Configuración de rutas
app.include_router(configure_routes(user_service))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3002)