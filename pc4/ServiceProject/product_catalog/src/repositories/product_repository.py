from .base_repository import BaseRepository
from ..schemas.product import ProductCreate, Product

class ProductRepository(BaseRepository): # Implementación del repositorio de productos
    def __init__(self):
        self.products = []
        self.next_id = 1

    # -- Leer --
    async def get_all(self):
        return self.products

    async def get_by_id(self, id: int):
        for product in self.products:
            if product.id == id:
                return product
        return None

    # -- Crear --
    async def create(self, product_data: ProductCreate):
        # Crea un nuevo producto con un ID autoincrementable
        product = Product(
            id=self.next_id,
            **product_data.model_dump() # Desempaqueta los datos del producto
        )
        self.products.append(product)
        self.next_id += 1
        return product

    # -- Actualizar --
    async def update(self, id: int, product_data: ProductCreate):
        product = await self.get_by_id(id)
        if product:
            index = self.products.index(product)
            updated_data = product_data.model_dump()
            updated_data['id'] = id
            self.products[index] = Product(**updated_data)
            return self.products[index]
        return None

    # -- Eliminar --
    async def delete(self, id: int):
        product = await self.get_by_id(id)
        if product:
            self.products.remove(product)
            return True
        return False 