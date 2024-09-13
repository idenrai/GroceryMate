from pydantic import BaseModel
from typing import List
from uuid import UUID


class ShoppingListItemBase(BaseModel):
    product_id: UUID
    quantity: int


class ShoppingListItemCreate(ShoppingListItemBase):
    pass


class ShoppingListItem(ShoppingListItemBase):
    item_id: UUID
    list_id: UUID

    class Config:
        orm_mode: True


class ShoppingListBase(BaseModel):
    list_name: str


class ShoppingListCreate(ShoppingListBase):
    items: List[ShoppingListItemCreate] = []


class ShoppingList(ShoppingListBase):
    list_id: UUID
    user_id: UUID
    items: List[ShoppingListItem] = []

    class Config:
        orm_mode: True
