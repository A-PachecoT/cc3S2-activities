from pydantic import BaseModel, Field
from typing import Optional

# Esquema base con campos comunes
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)

# Esquema para crear productos (sin ID)
class ProductCreate(ProductBase):
    pass

# Esquema completo del producto (con ID)
class Product(ProductBase):
    id: int
