# Rutas CRUD para productos

from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.product import Product, ProductCreate
from ..services.product_service import ProductService
from ..repositories.product_repository import ProductRepository

router = APIRouter(prefix="/products")

# Singleton del repositorio y servicio
product_repository = ProductRepository()
product_service = ProductService(product_repository)

@router.get("/", response_model=List[Product])
async def get_products():
    return await product_service.get_all()

@router.get("/{id}", response_model=Product)
async def get_product(id: int):
    product = await product_service.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate):
    return await product_service.create(product)

@router.put("/{id}", response_model=Product)
async def update_product(id: int, product: ProductCreate):
    updated_product = await product_service.update(id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@router.delete("/{id}")
async def delete_product(id: int):
    if not await product_service.delete(id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}