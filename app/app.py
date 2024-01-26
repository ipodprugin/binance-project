from fastapi import FastAPI
from .api.v1.routes import router as v1_router


app = FastAPI(
    swagger_ui_parameters={"displayRequestDuration": True}
)
app.include_router(v1_router, prefix="/api")

