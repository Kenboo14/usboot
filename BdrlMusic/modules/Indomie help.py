from pyrogram import *
from pyrogram.types import *

from BdrlMusic import *
from config import *

help_admin = [
    f"""
<b>HELP ADMIN GLOBAL

Perintah:
         <code>{PREFIXES[0]}gban</code> [user_id/username/reply to user]
Penjelasan:
           Untuk banned user dari semua group chat 

Perintah:
         <code>{PREFIXES[0]}ungban</code> [user_id/username/reply to user]
Penjelasan:
           Untuk unbanned user dari semua group chat</b>
""",
    f"""
<b>HELP ADMIN RESTRICT

Perintah:
         <code>{PREFIXES[0]}kick</code> [user_id/username/reply user]
Penjelasan:
           Untuk menendang anggota dari grup 

Perintah:
         <code>{PREFIXES[0]}ban</code> [user_id/username/reply user]
Penjelasan:
           Untuk memblokir anggota dari grup 

Perintah:
         <code>{PREFIXES[0]}mute</code> [user_id/username/reply user]
Penjelasan:
           Untuk membisukan anggota dari grup 

Perintah:
         <code>{PREFIXES[0]}unban</code> [user_id/username/reply user]
Penjelasan:
           Untuk melepas pemblokiran anggota dari grup 

Perintah:
         <code>{PREFIXES[0]}unmute</code> [user_id/username/reply user]
Penjelasan:
           Untuk melepas pembisuan anggota dari grup</b>
""",
]
help_next = [
    f"""<b>Haloo</b>
    
    """,
]
help_previous = [
    f"""<b>Haloo</b>
    
    """,
]
help_limit = [
    f"""<b>HELP LIMIT 
    
Perintah:
        <code>{PREFIXES[0]}limit</code> [Burung Puyuh]
Penjelasan:
        Gaada penjelasan, pasti kalian udh tau kan panteq?
        <b> kau ketik aja </b> <code>{PREFIXES[0]}limit</code> nanti juga bisa cok!</b>
    """,

]
help_play = [
   f"""<b>HELP PLAY
    
Perintah:
        <code>{PREFIXES[0]}play</code> [Judul lagu]
Penjelasan:
        Silahkan ketik <code>{PREFIXES[0]}play</code> beserta judul lagu</b>
    """,
]

help_sticker = [
    f"""<b>HELP STICKER KANG

Perintah:
         <code>{PREFIXES[0]}kang</code> [reply to image/sticker]
Penjelasan:
           Balas Ke Sticker Atau Gambar Untuk Menambahkan Ke Sticker Pack.
           Untuk Menambahkan dan costum emoji sticker Ke Sticker Pack Mu,
           <b>NOTE:</b> Untuk Membuat Sticker Pack baru Gunakan angka dibelakang <code>{PREFIXES[0]}kang</code>,
           <b>CONTOH:</b> <code>{PREFIXES[0]}kang</code> 2</code> untuk membuat dan menyimpan ke sticker pack ke 2</b>
""",
    f"""
<b>HELP STICKER MEMIFY 

Perintah:
         <code>{PREFIXES[0]}mmf</code> [text]
Penjelasan:
           Balas Ke Sticker atau Foto akan Di ubah menjadi sticker teks meme yang di tentukan.</b>
""",
    f"""
<b>HELP STICKER MEMES 

Perintah:
         <code>{PREFIXES[0]}memes</code> [text]
Penjelasan:
           Untuk membuat stiker memes random</b>
""",
    f"""
<b>HELP STICKER QUOTLY 

Perintah:
         <code>{PREFIXES[0]}q</code> [text/reply to text/media]
Penjelasan:
           Untuk merubah text menjadi sticker</b>
""",
    f"""
<b>HELP STICKER TINY 

Perintah:
         <code>{PREFIXES[0]}tiny</code> [reply to sticker]
Penjelasan:
           Untuk merubah sticker menjadi kecil</b>
""",
]

help_text = {
    "global": help_admin[0],
    "restrict": help_admin[1],
    "kang": help_sticker[0],
    "memify": help_sticker[1],
    "memes": help_sticker[2],
    "quotly": help_sticker[3],
    "tiny": help_sticker[4],
    "limit": help_limit[0],
    "play": help_play[0],
}


@ubot.on_message(filters.me & filters.command("help", PREFIXES))
async def _(client, message):
    if len(message.command) < 2:
        x = await client.get_inline_bot_results(bot.me.username, "user_help_command")
        try:
            return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            return await message.reply(error)
    else:
        if message.command[1] in help_text:
            return await message.reply(help_text[message.command[1]])


@bot.on_inline_query(filters.regex("^user_help_command"))
async def _(client, inline_query):
    button = [
        [
            InlineKeyboardButton("Globals", callback_data="admin admin_gban"),
            InlineKeyboardButton("Kangcut", callback_data="sticker sticker_kang"),
        ],
        [
            InlineKeyboardButton("Memify", callback_data="sticker sticker_memify"),
            InlineKeyboardButton("Memes", callback_data="sticker sticker_memes"),
        ],
        [
            InlineKeyboardButton("Quotly", callback_data="sticker sticker_quotly"),
            InlineKeyboardButton("Restrict", callback_data="admin admin_restrict"),
        ],
        [
            InlineKeyboardButton("Tiny", callback_data="sticker sticker_tiny"),
            InlineKeyboardButton("Limit", callback_data="limit limited"),
        ],
        [
            InlineKeyboardButton("<", callback_data="next next_nih"),
            InlineKeyboardButton(">", callback_data="previous previous_nih"),
        ],
    ]
    msg = "<b>HELP MENU OPEN\nPREFIXES: <code>NothingBot</code></b>"
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


@bot.on_callback_query(filters.regex("^admin"))
async def _(client, callback_query):
    for my in ubot._ubot:
        if callback_query.from_user.id == my.me.id:
            data = callback_query.data.split()[1]
            button = [
                [InlineKeyboardButton("• Mbalik •", callback_data="admin admin_back")]
            ]
            if data == "admin_gban":
                msg = help_admin[0]
            if data == "admin_restrict":
                msg = help_admin[1]
            if data == "admin_back":
                button = [
        [
            InlineKeyboardButton("Globals", callback_data="admin admin_gban"),
            InlineKeyboardButton("Kangcut", callback_data="sticker sticker_kang"),
        ],
        [
            InlineKeyboardButton("Memify", callback_data="sticker sticker_memify"),
            InlineKeyboardButton("Memes", callback_data="sticker sticker_memes"),
        ],
        [
            InlineKeyboardButton("Quotly", callback_data="sticker sticker_quotly"),
            InlineKeyboardButton("Restrict", callback_data="admin admin_restrict"),
        ],
        [
            InlineKeyboardButton("Tiny", callback_data="sticker sticker_tiny"),
            InlineKeyboardButton("Limit", callback_data="limit limited"),
        ],
        [
            InlineKeyboardButton("<", callback_data="next next_nih"),
            InlineKeyboardButton(">", callback_data="previous previous_nih"),
        ],
                ]
                msg = "<b>HELP MENU OPEN\nPREFIXES: <code>. , : ; !</code></b>"
            await callback_query.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(button)
            )


@bot.on_callback_query(filters.regex("^sticker"))
async def _(client, callback_query):
    for my in ubot._ubot:
        if callback_query.from_user.id == my.me.id:
            data = callback_query.data.split()[1]
            button = [
                [
                    InlineKeyboardButton(
                        "• Mbalik •", callback_data="sticker sticker_back"
                    )
                ]
            ]
            if data == "sticker_kang":
                msg = help_sticker[0]
            if data == "sticker_memify":
                msg = help_sticker[1]
            if data == "sticker_memes":
                msg = help_sticker[2]
            if data == "sticker_quotly":
                msg = help_sticker[3]
            if data == "sticker_tiny":
                msg = help_sticker[4]
            if data == "sticker_back":
                button = [
                    [
            InlineKeyboardButton("Globals", callback_data="admin admin_gban"),
            InlineKeyboardButton("Kangcut", callback_data="sticker sticker_kang"),
        ],
        [
            InlineKeyboardButton("Memify", callback_data="sticker sticker_memify"),
            InlineKeyboardButton("Memes", callback_data="sticker sticker_memes"),
        ],
        [
            InlineKeyboardButton("Quotly", callback_data="sticker sticker_quotly"),
            InlineKeyboardButton("Restrict", callback_data="admin admin_restrict"),
        ],
        [
            InlineKeyboardButton("Tiny", callback_data="sticker sticker_tiny"),
            InlineKeyboardButton("Limit", callback_data="limit limited"),
        ],
        [
            InlineKeyboardButton("<", callback_data="next next_nih"),
            InlineKeyboardButton(">", callback_data="previous previous_nih"),
        ],
                ]
                msg = "<b>HELP MENU OPEN\nPREFIXES: <code>. , : ; !</code></b>"
            await callback_query.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(button)
            )
@bot.on_callback_query(filters.regex("^limit"))
async def _(client, callback_query):
    for my in ubot._ubot:
        if callback_query.from_user.id == my.me.id:
            data = callback_query.data.split()[1]
            button = [
                [InlineKeyboardButton("• Mbalik •", callback_data="play limit_back")]
            ]
            if data == "limited":
                msg = help_limit[1]   
            if data == "limit_back":
                button = [
                    [
            InlineKeyboardButton("Globals", callback_data="admin admin_gban"),
            InlineKeyboardButton("Kangcut", callback_data="sticker sticker_kang"),
        ],
        [
            InlineKeyboardButton("Memify", callback_data="sticker sticker_memify"),
            InlineKeyboardButton("Memes", callback_data="sticker sticker_memes"),
        ],
        [
            InlineKeyboardButton("Quotly", callback_data="sticker sticker_quotly"),
            InlineKeyboardButton("Restrict", callback_data="admin admin_restrict"),
        ],
        [
            InlineKeyboardButton("Tiny", callback_data="sticker sticker_tiny"),
            InlineKeyboardButton("Limit", callback_data="limit limited"),
        ],
        [
            InlineKeyboardButton("<", callback_data="next next_nih"),
            InlineKeyboardButton(">", callback_data="previous previous_nih"),
        ],
                ]
                msg = "<b>HELP MENU OPEN\nPREFIXES: <code>. , : ; !</code></b>"
            await callback_query.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(button)
            )

