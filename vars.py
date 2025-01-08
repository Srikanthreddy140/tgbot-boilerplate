from os import getenv
class Settings:
    API_ID  :int = int(getenv("API_ID", 0))
    API_HASH  : str = str(getenv("API_HASH" , ""))
    BOT_TOKEN : str = str(getenv("BOT_TOKEN" , ""))
    MONGO_URI : str= str(getenv("MONGO_URL" , ""))
    ADMIN : int= int(getenv("ADMIN" , 89)
)
settings = Settings()