from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)  # type: ignore
        self.uri = uri
        self.db_name = db_name

    # your async functions here

db = MongoDB("mongodb://localhost:27017", "devdotpy")