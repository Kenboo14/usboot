from datetime import datetime

from pyrogram import enums, filters
from pyrogram.types import Message

from BdrlMusic import ubot
from BdrlMusic.utils import dbfunctions as TOMI
from config import PREFIXES

from pyrogram import * 
from pyrogram.types import * 
  
from BdrlMusic import * 
from config import *

log = []

__MODULE__ = "NOTES"
__HELP__ = (
    f"""
Perintah:
         <code>{PREFIXES[0]}save</code> [note_name - reply]
Penjelasan:
           Untuk menyimpan sebuah catatan 

Perintah:
         <code>{PREFIXES[0]}get</code> [note_name]
Penjelasan:
           Untuk mendapatkan catatan yang disimpan 

Perintah:
         <code>{PREFIXES[0]}delnote</code> [note_name]
Penjelasan:
           Untuk menghapus catatan 

Perintah:
         <code>{PREFIXES[0]}notes</code>
Penjelasan:
           Untuk melihat daftar catatan yang disimpan 
""",
)

getpay_payment = [
    f"""<b>INI DANA</b>
""",
    f"""<b>INI BCA</b>
""",
]

getpay_text = {
    "paymont": getpay_payment[0],
    "payment": getpay_payment[1],
}


@ubot.on_message(filters.command(["stats", "status"], PREFIXES) & filters.me)
async def stats(_, message: Message):
    Man = await message.reply("<code>Collecting stats...</code>")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await _.get_me()
    async for dialog in _.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Man.edit(
        """<b>Your Stats Obtained in</b> <code>{}</code> <b>seconds</b>
<b>You have</b> <code>{}</code> <b>Private Messages.</b>
<b>You are in</b> <code>{}</code> <b>Groups.</b>
<b>You are in</b> <code>{}</code> <b>Super Groups.</b>
<b>You Are in</b> <code>{}</code> <b>Channels.</b>
<b>You Are Admin in</b> <code>{}</code> <b>Chats.</b>
<b>Bots =</b> <code>{}</code>""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@ubot.on_message(filters.command("save", PREFIXES) & filters.me)
async def _(client, message):
    note_name = get_arg(message)
    reply = message.reply_to_message
    if not note_name:
        return await message.reply("lo goblok atau gimana?")
    if not reply:
        return await message.reply(
            "Balas pesan dan nama note pada catatan untuk menyimpan catatan"
        )
    if await TOMI.get_note(f"{client.me.id}_{note_name}"):
        return await message.reply(f"Note <code>{note_name}</code> sudah disimpan")
    copy = await client.copy_message(client.me.id, message.chat.id, reply.id)
    await TOMI.save_note(f"{client.me.id}_{note_name}", copy.id)
    await client.send_message(
        client.me.id,
        f"👆🏻 Pesan diatas ini jangan dihapus\n\n👉🏻 Ketik: <code>{PREFIXES[0]}get {note_name}</code>",
    )
    await message.reply(f"Note <code>{note_name}</code> berhasil di simpan")


@ubot.on_message(filters.command("get", PREFIXES) & filters.me)
async def _(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("lo goblok atau gimana?")
    note = await TOMI.get_note(f"{client.me.id}_{note_name}")
    if not note:
        return await message.reply(f"Note <code>{note_name}</code> Tidak ditemukan")
    if message.reply_to_message:
        await client.copy_message(
            message.chat.id,
            client.me.id,
            note,
            reply_to_message_id=message.reply_to_message_id,
        )
    else:
        await client.copy_message(
            message.chat.id, client.me.id, note, reply_to_message_id=message.id
        )


@ubot.on_message(filters.command("getpay", PREFIXES) & filters.me)
async def _(client, message):

    if len(message.command) < 2:
        x = await client.get_inline_bot_results(bot.me.username, "user_getpay_command")
        try:
            return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            return await message.reply(error)
    else:
        if message.command[1] in getpay_text:
            return await message.reply(getpay_text[message.command[1]])


@bot.on_inline_query(filters.regex("^user_getpay_command"))
async def _(client, inline_query):
    button = [
        [
            InlineKeyboardButton("DANA", callback_data="payment paymont"),
            InlineKeyboardButton("BCA", callback_data="payment payment"),
        ],
     ]
     msg = "<b>HELP MENU OPEN\nSUPPORT BY SEEKUT CORP: <code>. , : ; !</code></b>"
     await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(button),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )
@bot.on_callback_query(filters.regex("^payment"))
async def _(client, callback_query):
    for my in ubot._ubot:
        if callback_query.from_user.id == my.me.id:
            data = callback_query.data.split()[1]
            button = [
                [
                    InlineKeyboardButton(
                        "• KEMBALI •", callback_data="payment payment_back"
                    )
                ]
            ]
            if data == "paymont":
                msg = getpay_payment[0]
            if data == "payment":
                msg = getpay_payment[1]
            if data == "payment_back":
                button = [
                    [
                        InlineKeyboardButton("DANA", callback_data="payment paymont"),
                        InlineKeyboardButton("BCA", callback_data="payment payment"),
                    ],
                ]
            msg = "<b>HELP MENU OPEN\nSUPPORT BY SEEKUT CORP: <code>. , : ; !</code></b>"
            await client.answer_callback_query(
        callback_query.id,
        cache_time=0,
)

@ubot.on_message(filters.command("delnote", PREFIXES) & filters.me)
async def _(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("Mau hapus yang mana dek?")
    note = await TOMI.get_note(f"{client.me.id}_{note_name}")
    if not note:
        return await message.reply(f"Gagal menghapus note <code>{note_name}</code>")
    await TOMI.rm_note(f"{client.me.id}_{note_name}")
    await message.reply(f"Berhasil menghapus note <code>{note_name}</code>")
    await client.delete_messages(client.me.id, [int(note), int(note) + 1])


@ubot.on_message(filters.command("notes", PREFIXES) & filters.me)
async def _(client, message):
    msg = f"<b>List of saved notes:</b>\n"
    all_notes = await TOMI.all_notes()
    for notes in all_notes:
        if client.me.id == int(notes.split("_", 1)[0]):
            msg += f"-<code>{notes.split('_', 1)[1]}</code>\n"
        else:
            msg += ""
    await message.reply(msg)


@ubot.on_message(filters.command(["kickme", "kikmi"], PREFIXES) & filters.me)
async def kikmi(client, message):
    await message.reply("test")
    await client.leave_chat(message.chat.id)


@ubot.on_message(filters.media & filters.private)
async def get_dest(c, m):
    # To save Self-Destructing photo
    if m.photo and m.photo.ttl_seconds:
        photo = await m.download()
        return await c.send_photo(f"{client.me.id}", photo)

    # To save Self-Destructing Video
    if m.video and m.video.ttl_seconds:
        video = await m.download()
        return await c.send_video(f"{client.me.id}", video)
