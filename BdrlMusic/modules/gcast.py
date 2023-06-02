print("Install gcast.py")
import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import BadRequest
from pyrogram.types import Message

from BdrlMusic import bot, ubot
from config import *


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)


BLACKLIST_CHAT = [-1001459812644, -1001692751821, -1001813669338]


__MODULE__ = "GCAST"
__HELP__ = f"""
Perintah:
         <code>{PREFIXES[0]}gucast</code> [text/reply to text/media]
Penjelasan:
           Untuk mengirim pesan ke semua user 

Perintah:
         <code>{PREFIXES[0]}gcast</code> [text/reply to text/media]
Penjelasan:
           Untuk mengirim pesan ke semua group 
"""


@ubot.on_message(filters.me & filters.command("gcast", PREFIXES))
async def _(client, message: Message):
    sent = 0
    failed = 0
    msg = await message.reply(
        "<code>Limit Jangan salahin Gua tod, Proses menyebarkan pesan...</code>"
    )
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    return await message.reply("<b>Pesannya Mana ngentod</b>")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in BLACKLIST_CHAT:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(3)
    await msg.edit(
        f"<b>Berhasil Mengirim Pesan Ke</b> <code>{sent}</code> <b>Grup, Gagal Mengirim Pesan Ke</b> <code>{failed}</code> <b>Grup</b>"
    )


@ubot.on_message(filters.me & filters.command("gucast", PREFIXES))
async def _(client, message: Message):
    sent = 0
    failed = 0
    msg = await message.reply(
        "<code>Limit Jangan salahin Gua tod, Proses menyebarkan pesan...</code>"
    )
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    return await message.reply("<b>Pesannya Mana ngentod</b>")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in BLACKLIST_CHAT:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(3)
    await msg.edit(f"✅ Berhasil Terkirim: {sent} \n❌ Gagal Terkirim: {failed}")


@bot.on_message(filters.user(OWNER_ID) & filters.command("send"))
@ubot.on_message(filters.me & filters.command("send", PREFIXES))
async def _(client, message: Message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        try:
            await message.reply_to_message.copy(chat_id)
            tm = await message.reply(f"✅ Berhasil Dikirim Ke {chat_id}")
            await asyncio.sleep(2.5)
            await message.delete()
            await tm.delete()
        except BadRequest as t:
            await message.reply(f"{t}")
            return
    try:
        chat_id = message.text.split(None, 2)[1]
        chat_send = message.text.split(None, 2)[2]
    except Exception as e:
        await message.reply(f"{e}")
    if len(chat_send) >= 2:
        try:
            await client.send_message(chat_id, chat_send)
            tm = await message.reply(f"✅ Berhasil Dikirim Ke {chat_id}")
            await asyncio.sleep(2.5)
            await message.delete()
            await tm.delete()
        except BadRequest as t:
            await message.reply(f"{t}")
