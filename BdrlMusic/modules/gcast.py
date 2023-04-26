print("Install gcast.py")
import asyncio

import dotenv
from pyrogram import enums, filters
from requests import get

from config import BLACKLIST_GCAST
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import BadRequest
from pyrogram.types import Message

from BdrlMusic.Helpers.basic import edit_or_reply
from BdrlMusic.Helpers.tools import get_arg
from BdrlMusic import bot, ubot
from config import *

HAPP = None

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/Kenboo14/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001872496207, -1001741405741, -1001675452200]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


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
Perintah:
         <code>{PREFIXES[0]}blchat</code> [text/reply to text/media]
Penjelasan:
           Untuk melihat list blacklist group 
Perintah:
         <code>{PREFIXES[0]}addblacklist</code> [text/reply to text/media]
Penjelasan:
           Untuk memberi penegcualian fitur gikes ke semua group 
Perintah:
         <code>{PREFIXES[0]}delblacklist</code> [text/reply to text/media]
Penjelasan:
           Untuk menghapus ditur addblacklist ke group yang sudah masuk blacklist gikes 
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



@ubot.on_message(filters.me & filters.command("blchat", PREFIXES))
async def _(client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    list = BLACKLIST_GCAST.replace(" ", " \n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            message,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `{PREFIXES}addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_or_reply(message, "🔮 **Blacklist GCAST:** `Disabled`")


@ubot.on_message(filters.me & filters.command("addblacklist", PREFIXES))
async def _(client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{message.chat.id}` **ke daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    if await in_heroku():
        heroku_var = HAPP.config()
        heroku_var["BLACKLIST_GCAST"] = blacklistgrup
    else:
        path = dotenv.find_dotenv("config.env")
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    restart()



@ubot.on_message(filters.me & filters.command("delblacklist", PREFIXES))
async def _(client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    gett = str(message.chat.id)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{message.chat.id}` **dari daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        if await in_heroku():
            heroku_var = HAPP.config()
            heroku_var["BLACKLIST_GCAST"] = blacklistgrup
        else:
            path = dotenv.find_dotenv("config.env")
            dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
        restart()
    else:
        await xxnx.edit("**Grup ini tidak ada dalam daftar blacklist gcast.**")


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
