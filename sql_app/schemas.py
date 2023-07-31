import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BaseSchemas(BaseModel):

    title: Optional[str]
    description: Optional[str]


class BaseSchemasAllCreate(BaseSchemas):
    pass


class BaseSchemasAllReturn(BaseSchemas):
    id: uuid.UUID


class DishSchemas(BaseSchemas):
    price: Decimal

    class Config:
        from_attributes = True


class DishSchemasReturn(DishSchemas):
    id: uuid.UUID

    class Config:
        from_attributes = True


class SubmenuSchemas(BaseSchemasAllReturn):
    dishes_count: int = 0

    class Config:
        from_attributes = True


class MenuSchemas(BaseSchemasAllReturn):
    submenus_count: int = 0
    dishes_count: int = 0

    class Config:
        from_attributes = True


class MenuSchemasGreate(BaseSchemas):
    class Config:
        from_attributes = True