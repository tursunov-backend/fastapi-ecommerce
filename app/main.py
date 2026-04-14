from fastapi import FastAPI

# test
from app.db.session import get_db


app = FastAPI(title="Ecommerce")

session = next(get_db())
print(session.connection())
