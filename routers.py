from fastapi import APIRouter
from endpoints import home_page, prediction

router = APIRouter()

router.include_router(home_page.router, tags=["Home"])
router.include_router(prediction.router, tags=["Prediction"])