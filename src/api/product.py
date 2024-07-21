from fastapi import FastAPI, HTTPException, APIRouter # type: ignore
# from fastapi.staticfiles import StaticFiles # type: ignore
from pydantic import BaseModel # type: ignore
from api.db import get_db_connection

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
router = APIRouter()
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    category: str

# @router.get("/products", response_model=list[router])
@router.get("")
def get_products():
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Product")

    products = cursor.fetchall()
    cursor.close()
    connection.close()

    return products

# if __name__ == "__main__":
#     import uvicorn # type: ignore
#     uvicorn.run(app, host="127.0.0.1", port=8000)
