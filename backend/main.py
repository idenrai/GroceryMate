from fastapi import FastAPI
from routers import shopping_list

app = FastAPI()

app.include_router(shopping_list.router)
