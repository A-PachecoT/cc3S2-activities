from fastapi import FastAPI
from src.routers import product_router

app = FastAPI(
    title="Catálogo de Productos API",
    description="API para gestión de catálogo de productos",
    version="1.0.0"
)

# Incluir routers
app.include_router(product_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
