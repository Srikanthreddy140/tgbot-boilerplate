from pyrogram.client import Client
from vars import settings

class Bot(Client):
    def __init__(self) -> None:
        super().__init__( #type:ignore
            name="gptt",
            api_id=settings.API_ID,
            api_hash=settings.API_HASH,
            bot_token=settings.BOT_TOKEN,
            workers=3,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self): # type: ignore
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(
                settings.ADMIN, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**"
            )
    async def stop(self, *args): # type: ignore
        await super().stop()
        print("Stopped.....")


Bot().run() #type:ignore