from pyrogram import filters

from BdrlMusic import bot, ubot
from config import PREFIXES


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@bot.on_message(filters.command("copy"))
@ubot.on_message(filters.command("copy", PREFIXES) & filters.me)
async def _(client, message):
    msg = message.reply_to_message or message
    Tm = await message.reply("Tunggu sebentar")
    await Tm.delete()
    link = get_arg(message)
    if not link:
        return await message.reply(
            f"<b><code>{message.text}</code> [link_konten_telegram]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id, reply_to_message_id=msg.id)
        except Exception as error:
            await message.reply(error)
    else:
        await message.reply("masukkin link yang valid")
