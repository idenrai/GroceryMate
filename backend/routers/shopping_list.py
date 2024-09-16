from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from schemas.shopping_list import ShoppingList, ShoppingListCreate
from crud.shopping_list import (
    create_shopping_list,
    get_shopping_list,
    update_shopping_list,
    delete_shopping_list,
)
from database import get_db
from typing import Generator

router = APIRouter()


@router.post("/shopping-lists", response_model=ShoppingList)
def create_shopping_list_endpoint(
    shopping_list: ShoppingListCreate, db: Generator = Depends(get_db)
):
    # TODO: user_id 구현
    user_id = "43401d31-f674-4bee-8c43-cfb5b8b8c18b"
    return create_shopping_list(db, shopping_list, user_id=user_id)


@router.get("/shopping-lists/{shopping_list_id}", response_model=ShoppingList)
def get_shopping_list_endpoint(shopping_list_id: UUID, db: Generator = Depends(get_db)):
    shopping_list = get_shopping_list(db, shopping_list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    return shopping_list


@router.put("/shopping-lists/{shopping_list_id}", response_model=ShoppingList)
def update_shopping_list_endpoint(
    shopping_list_id: UUID,
    shopping_list: ShoppingListCreate,
    db: Generator = Depends(get_db),
):
    updated_shopping_list = update_shopping_list(db, shopping_list_id, shopping_list)
    if not updated_shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    return updated_shopping_list


@router.delete("/shopping-lists/{shopping_list_id}")
def delete_shopping_list_endpoint(
    shopping_list_id: UUID, db: Generator = Depends(get_db)
):
    delete_shopping_list(db, shopping_list_id)
    return {"message": "Shopping list deleted successfully"}
    return {"message": "Shopping list deleted successfully"}
