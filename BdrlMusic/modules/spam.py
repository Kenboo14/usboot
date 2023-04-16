import asyncio

from pyrogram import filters

from BdrlMusic import ubot
from config import OWNER_ID, PREFIXES


@ubot.on_message(filters.command("spam", PREFIXES) & filters.user(OWNER_ID))
@ubot.on_message(filters.command("spam", PREFIXES) & filters.me)
async def _(client, message):
    if message.reply_to_message:
        spam = await message.reply("Diproses")
        reply_id = message.reply_to_message.id
        quantity = int(message.text.split(None, 2)[1])
        spam_text = message.text.split(None, 2)[2]
        await asyncio.sleep(1)
        await message.delete()
        await spam.delete()
        for i in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_id
            )
            await asyncio.sleep(0.1)
    else:
        if len(message.command) < 2:
            await message.reply_text("⚡ Usage:\n !spam jumlah spam, text spam")
        else:
            spam = await message.reply("Diproses")
            quantity = int(message.text.split(None, 2)[1])
            spam_text = message.text.split(None, 2)[2]
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for i in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(0.1)
