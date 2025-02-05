from os import getenv
class Settings:
    API_ID  :int = int(getenv("API_ID", 20154522))
    API_HASH  : str = str(getenv("API_HASH" , "ec1b720c2e0035a310d47ebd5655b676"))
    BOT_TOKEN : str = str(getenv("BOT_TOKEN" , "7887189932:AAE2lr7LQDk2zsrYcYjmRyuWFAAgwT6oLF8"))
    MONGO_URI : str= str(getenv("MONGO_URL" , "mongodb+srv://royalsrikanth140:n0O97ntpssfJWUjX@cluster0.788gy1y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    ADMIN : int= int(getenv("ADMIN" , 7003079691)
)
settings = Settings()
