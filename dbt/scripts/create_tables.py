import duckdb

# DuckDB 데이터베이스 파일에 연결
con = duckdb.connect("../grocery_mate.db")


# 각 테이블 생성 함수
def create_tables():
    try:
        # Users 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                user_id UUID PRIMARY KEY,
                username VARCHAR(100),
                email VARCHAR(100),
                location VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        print("Users 테이블 생성 완료")

        # Stores 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Stores (
                store_id UUID PRIMARY KEY,
                store_name VARCHAR(100),
                location VARCHAR(100),
                flyer_image BLOB
            )
        """
        )
        print("Stores 테이블 생성 완료")

        # Products 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                product_id UUID PRIMARY KEY,
                product_name VARCHAR(100),
                category VARCHAR(50)
            )
        """
        )
        print("Products 테이블 생성 완료")

        # Prices 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Prices (
                price_id UUID PRIMARY KEY,
                product_id UUID REFERENCES Products(product_id),
                store_id UUID REFERENCES Stores(store_id),
                price FLOAT,
                date_recorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                source VARCHAR(100)
            )
        """
        )
        print("Prices 테이블 생성 완료")

        # ShoppingLists 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS ShoppingLists (
                list_id UUID PRIMARY KEY,
                user_id UUID REFERENCES Users(user_id),
                list_name VARCHAR(100),
                total_estimated_price FLOAT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        print("ShoppingLists 테이블 생성 완료")

        # ShoppingListItems 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS ShoppingListItems (
                item_id UUID PRIMARY KEY,
                list_id UUID REFERENCES ShoppingLists(list_id),
                product_id UUID REFERENCES Products(product_id),
                quantity INT,
                estimated_price FLOAT
            )
        """
        )
        print("ShoppingListItems 테이블 생성 완료")

        # Favorites 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Favorites (
                user_id UUID REFERENCES Users(user_id),
                store_id UUID REFERENCES Stores(store_id),
                PRIMARY KEY (user_id, store_id)
            )
        """
        )
        print("Favorites 테이블 생성 완료")

        # Recipes 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS Recipes (
                recipe_id UUID PRIMARY KEY,
                recipe_name VARCHAR(100),
                description TEXT,
                instructions TEXT
            )
        """
        )
        print("Recipes 테이블 생성 완료")

        # RecipeIngredients 테이블 생성
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS RecipeIngredients (
                ingredient_id UUID PRIMARY KEY,
                recipe_id UUID REFERENCES Recipes(recipe_id),
                product_id UUID REFERENCES Products(product_id),
                quantity INT
            )
        """
        )
        print("RecipeIngredients 테이블 생성 완료")

    except Exception as e:
        print(f"오류 발생: {e}")


# 테이블 생성 실행
create_tables()

# 연결 종료
con.close()
