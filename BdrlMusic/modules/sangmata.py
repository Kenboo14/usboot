import asyncio

from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import Message

from BdrlMusic import ubot
from BdrlMusic.utils.function import extract_users
from config import PREFIXES


@ubot.on_message(filters.command(["sg", "sa"], PREFIXES) & filters.me)
async def _(_, message: Message):
    args = await extract_users(message)
    lol = await message.reply(
        "<code>LU SIAPA SI KENTOT, GUA KEPO, GA SENENG PC!!</code>"
    )
    if not args:
        return await lol.edit("<b>user tidak ditemukan</b>")
    try:
        user = await _.get_users(args)
    except Exception:
        return await lol.edit(
            "<code>Reply Ke Pesan User Yang Kau Pengen KEPOIN ngentot.</code>"
        )
    bot = "SangMata_beta_bot"
    try:
        txt = await _.send_message(bot, f"/search_id {user.id}")
    except YouBlockedUser:
        await _.unblock_user(bot)
        txt = await _.send_message(bot, f"/search_id {user.id}")
    await asyncio.sleep(1)
    await txt.delete()
    await lol.delete()
    for getName in ["Name", "Username"]:
        async for getText in _.search_messages(bot, query=getName, limit=1):
            if getName not in getText.text:
                await message.reply(
                    f"<code>Masa Gua Gak Nemu Riwayat {getName} si ngentot, Wah si anjing belom pernah ganti apa apa su!!</code>"
                )
            else:
                await message.reply(getText.text)
