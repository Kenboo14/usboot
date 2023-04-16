import asyncio
from io import BytesIO

from pyrogram import filters

from BdrlMusic import aiosession, ubot
from config import PREFIXES


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@ubot.on_message(filters.command("carbon", PREFIXES) & filters.me)
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    ex = await message.reply("<code>Preparing Carbon</code>")
    carbon = await make_carbon(text)
    await ex.edit("<code>Uploading</code>")
    message.reply_to_message or message
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            reply_to_message_id=message.id,
        ),
    )
    carbon.close()
