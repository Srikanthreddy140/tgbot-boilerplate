import asyncio
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , Message

@Client.on_message(filters.command("start") & filters.incoming) #type: ignore
async def start(client:Client, message: Message):
    await message.reply_text( #type: ignore
        f"**__Hello {message.from_user.first_name}__**\nThis boilerplate is made by @devdotpy",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Help",
                        url="https://t.me/devdotpy"
                    ),
                    InlineKeyboardButton(
                        "Callback ping",
                        callback_data=f"ping#{message.from_user.id}"
                    )
                ]
            ]
        )
    )
    msg = await message.reply_text("I will be deleted in 5 seconds") #type: ignore
    await asyncio.sleep(5)
    await msg.delete()
