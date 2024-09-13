from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class ShoppingListItem(BaseModel):
    item_id: UUID
    list_id: UUID
    product_id: UUID
    quantity: int
    estimated_price: float


class ShoppingList(BaseModel):
    list_id: UUID
    user_id: UUID
    list_name: str
    total_estimated_price: float
    items: Optional[List[ShoppingListItem]] = []
