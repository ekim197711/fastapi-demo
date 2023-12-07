import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "Message": "This is running programmatically inside Python"
    }


async def main():
    config = uvicorn.Config("programmatic_start:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
