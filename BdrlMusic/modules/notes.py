import asyncio

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from BdrlMusic import ubot
from config import PREFIXES


@ubot.on_message(filters.command("notes", PREFIXES) & filters.me)
async def _(client, message):
    await client.unblock_user("Kippubot")
    bot_info = await client.resolve_peer("Kippubot")
    msg = await message.reply("<code>Processing . . .</code>")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await asyncio.sleep(1)
    status = await client.get_messages("Kippubot", response.updates[1].message.id + 1)
    await msg.edit(status.text)
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
