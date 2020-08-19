from fastapi import FastAPI
from database.setup import engine
from models import models
from routers import items, users


models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users."
    },
    {
        "name": "items",
        "description": "Operations with items."
    }
]

app = FastAPI(
    title="My App",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="0.0.1",
    openapi_tags=tags_metadata
)


app.include_router(items.router)
app.include_router(users.router)
