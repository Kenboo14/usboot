import asyncio

from pyrogram import filters
from BdrlMusic import ubot
from config import PREFIXES


@ubot.on_message(filters.command("notes", PREFIXES) & filters.me)
async def _(client, message):
    print ("JANCOK");
    print ("KONTOL");
