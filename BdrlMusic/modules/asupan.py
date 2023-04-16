import asyncio
from random import choice

from pyrogram import enums, filters
from pyrogram.types import Message

from BdrlMusic import ubot
from config import PREFIXES


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


@ubot.on_message(filters.command("asupan", PREFIXES) & filters.me)
async def asupan_cmd(client, message):
    await asyncio.gather(
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "IndomieGantengV3", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=message.id,
        ),
    )


@ubot.on_message(filters.command("ayang", PREFIXES) & filters.me)
async def asupan_cmd(client, message):
    await asyncio.gather(
        client.send_photo(
            message.chat.id,
            choice(
                [
                    asupan.photo.file_id
                    async for asupan in client.search_messages(
                        "IndomieGantengV2", filter=enums.MessagesFilter.PHOTO
                    )
                ]
            ),
            reply_to_message_id=message.id,
        ),
    )


@ubot.on_message(filters.command("ayang2", PREFIXES) & filters.me)
async def asupan_cmd(client, message):
    message.reply_to_message or message
    await asyncio.gather(
        client.send_photo(
            message.chat.id,
            choice(
                [
                    asupan.photo.file_id
                    async for asupan in client.search_messages(
                        "galeriCogann", filter=enums.MessagesFilter.PHOTO
                    )
                ]
            ),
            reply_to_message_id=message.id,
        ),
    )
