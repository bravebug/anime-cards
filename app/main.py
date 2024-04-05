from fastapi import FastAPI
import uvicorn
from app.routes.characters import character_router


app = FastAPI()

app.include_router(character_router)


if __name__ == '__main__':
    uvicorn.run(app)
