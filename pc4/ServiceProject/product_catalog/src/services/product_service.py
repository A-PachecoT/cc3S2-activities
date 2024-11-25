from .base_service import BaseService
from ..repositories.product_repository import ProductRepository
from ..schemas.product import Product, ProductCreate

class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, id: int):
        return await self.repository.get_by_id(id)

    async def create(self, product_data: ProductCreate):
        return await self.repository.create(product_data)

    async def update(self, id: int, product_data: ProductCreate):
        return await self.repository.update(id, product_data)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id) 