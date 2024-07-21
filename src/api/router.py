from fastapi import APIRouter # type: ignore
from api import product
router = APIRouter()

router.include_router(router=product.router, tags=["products"], prefix="/products")
