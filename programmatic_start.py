import asyncio

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

ID_GENERATOR = 10


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "Message": "This is running programmatically inside Python"
    }


class Alien(BaseModel):
    id: int
    type: str
    name: str
    weight: float


@app.post("/create")
def createAlien(alien: Alien):
    global ID_GENERATOR
    ID_GENERATOR = ID_GENERATOR + 1
    print(f"Create this alien ${alien}")
    print(f"This is a string ${alien.model_dump_json()}")
    newalien = Alien(id=ID_GENERATOR, type=alien.type, name=alien.name, weight=alien.weight)
    return newalien


async def main():
    config = uvicorn.Config("programmatic_start:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
