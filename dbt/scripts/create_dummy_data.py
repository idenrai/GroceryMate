import duckdb
import uuid

# DuckDB 데이터베이스 파일에 연결
con = duckdb.connect("../grocery_mate.db")


# 더미 데이터 삽입 함수
def insert_dummy_data():
    # Products 더미 데이터 삽입
    apple_product_id = str(uuid.uuid4())
    beef_product_id = str(uuid.uuid4())
    con.execute(
        f"""
        INSERT INTO Products (product_id, product_name, category)
        VALUES
        ('{apple_product_id}', 'Apple', 'Fruits'),
        ('{beef_product_id}', 'Beef', 'Meat')
    """
    )

    # Stores 더미 데이터 삽입
    walmart_store_id = str(uuid.uuid4())
    target_store_id = str(uuid.uuid4())
    con.execute(
        f"""
        INSERT INTO Stores (store_id, store_name, location)
        VALUES
        ('{walmart_store_id}', 'Walmart', 'New York'),
        ('{target_store_id}', 'Target', 'Los Angeles')
    """
    )

    # Prices 더미 데이터 삽입
    con.execute(
        f"""
        INSERT INTO Prices (price_id, product_id, store_id, price, source)
        VALUES
        ('{uuid.uuid4()}', '{apple_product_id}', '{walmart_store_id}', 0.99, 'Flyer'),
        ('{uuid.uuid4()}', '{beef_product_id}', '{target_store_id}', 4.99, 'Flyer')
    """
    )

    # Users 더미 데이터 삽입
    user1_id = str(uuid.uuid4())
    user2_id = str(uuid.uuid4())
    con.execute(
        f"""
        INSERT INTO Users (user_id, username, email, location)
        VALUES
        ('{user1_id}', 'John Doe', 'john@example.com', 'New York'),
        ('{user2_id}', 'Jane Smith', 'jane@example.com', 'Los Angeles')
    """
    )

    # ShoppingLists 더미 데이터 삽입
    shopping_list_id = str(uuid.uuid4())
    con.execute(
        f"""
        INSERT INTO ShoppingLists (list_id, user_id, list_name, total_estimated_price)
        VALUES
        ('{shopping_list_id}', '{user1_id}', 'Weekly Groceries', 50.00)
    """
    )

    # ShoppingListItems 더미 데이터 삽입
    con.execute(
        f"""
        INSERT INTO ShoppingListItems (item_id, list_id, product_id, quantity, estimated_price)
        VALUES
        ('{uuid.uuid4()}', '{shopping_list_id}', '{apple_product_id}', 5, 5.00)
    """
    )

    # Favorites 더미 데이터 삽입
    con.execute(
        f"""
        INSERT INTO Favorites (user_id, store_id)
        VALUES
        ('{user1_id}', '{walmart_store_id}'),
        ('{user2_id}', '{target_store_id}')
    """
    )

    # Recipes 더미 데이터 삽입
    recipe_id = str(uuid.uuid4())
    con.execute(
        f"""
        INSERT INTO Recipes (recipe_id, recipe_name, description, instructions)
        VALUES
        ('{recipe_id}', 'Apple Pie', 'Delicious apple pie recipe', '1. Preheat oven... 2. Mix ingredients...')
    """
    )

    # RecipeIngredients 더미 데이터 삽입
    con.execute(
        f"""
        INSERT INTO RecipeIngredients (ingredient_id, recipe_id, product_id, quantity)
        VALUES
        ('{uuid.uuid4()}', '{recipe_id}', '{apple_product_id}', 3)
    """
    )


# 더미 데이터 삽입 실행
insert_dummy_data()

# 연결 종료
con.close()
