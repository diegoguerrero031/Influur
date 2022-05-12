from fastapi import FastAPI
from routers import router
import uvicorn
import os

app = FastAPI(
    title="INFLUUR",
    description="Deploy of churn prediction model",
    version="1.0")

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, port=os.environ.get('PORT', 8080), host='0.0.0.0')