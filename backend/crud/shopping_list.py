from uuid import uuid4, UUID
from models.shopping_list import ShoppingList, ShoppingListItem
from schemas.shopping_list import ShoppingListCreate


def create_shopping_list(db, shopping_list: ShoppingListCreate, user_id: UUID):
    shopping_list_id = uuid4()
    db.execute(
        "INSERT INTO ShoppingLists (list_id, user_id, list_name, total_estimated_price) VALUES (?, ?, ?, ?)",
        (shopping_list_id, user_id, shopping_list.list_name, 0.0),
    )
    for item in shopping_list.items:
        item_id = uuid4()
        db.execute(
            "INSERT INTO ShoppingListItems (item_id, list_id, product_id, quantity, estimated_price) VALUES (?, ?, ?, ?, ?)",
            (item_id, shopping_list_id, item.product_id, item.quantity, 0.0),
        )
    return ShoppingList(
        list_id=shopping_list_id,
        user_id=user_id,
        list_name=shopping_list.list_name,
        total_estimated_price=0.0,
        items=shopping_list.items,
    )


def get_shopping_list(db, shopping_list_id: str):
    result = db.execute(
        "SELECT * FROM ShoppingLists WHERE list_id = ?", (shopping_list_id,)
    ).fetchone()
    if result:
        shopping_list = ShoppingList(
            list_id=result[0],
            user_id=result[1],
            list_name=result[2],
            total_estimated_price=result[3],
        )
        items = db.execute(
            "SELECT * FROM ShoppingListItems WHERE list_id = ?",
            (shopping_list_id,),
        ).fetchall()
        shopping_list.items = [
            ShoppingListItem(
                item_id=item[0],
                list_id=item[1],
                product_id=item[2],
                quantity=item[3],
                estimated_price=item[4],
            )
            for item in items
        ]
        return shopping_list
    return None


def update_shopping_list(db, shopping_list_id: UUID, shopping_list: ShoppingListCreate):
    db.execute(
        "UPDATE ShoppingLists SET list_name = ? WHERE list_id = ?",
        (shopping_list.list_name, shopping_list_id),
    )
    db.execute(
        "DELETE FROM ShoppingListItems WHERE list_id = ?",
        (shopping_list_id,),
    )
    for item in shopping_list.items:
        item_id = uuid4()
        db.execute(
            "INSERT INTO ShoppingListItems (item_id, list_id, product_id, quantity, estimated_price) VALUES (?, ?, ?, ?, ?)",
            (item_id, shopping_list_id, item.product_id, item.quantity, 0.0),
        )
    return get_shopping_list(db, shopping_list_id)


def delete_shopping_list(db, shopping_list_id: str):
    db.execute(
        "DELETE FROM ShoppingListItems WHERE list_id = ?",
        (shopping_list_id,),
    )
    db.execute("DELETE FROM ShoppingLists WHERE list_id = ?", (shopping_list_id,))
