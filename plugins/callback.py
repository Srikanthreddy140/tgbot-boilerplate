from pyrogram.client import Client 
from pyrogram.types import (CallbackQuery)
@Client.on_callback_query() # type: ignore
async def cb_handler(client: Client, query: CallbackQuery) -> None:
    clicker = int(query.data.split("#")[1]) if isinstance(query.data, str) else None
    data = query.data.split("#")[0] if isinstance(query.data, str) else None
    if clicker != query.from_user.id:
        return await query.answer( # type: ignore
            f"Hey {query.from_user.first_name}, Jaldi Yeha Se Hato", show_alert=True)
    elif data == "ping":
        await query.answer("Pong", show_alert=True)