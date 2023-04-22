from pyrogram import *
from pyrogram.types import *

from BdrlMusic import *
from config import *

help_payment = [
    f"""
<b>INI ADALAH PAYMENT DANA KENBO</b>
    """,
    f"""
<b>INI ADALAH PAYMENT BCA KENBO</b>
    """,
    ]         
            
payment_text = {
         "paymont": help_payment[0],
         "payment": help_payment[1],
         "paymint": help_payment[2],
         "paymunt": help_payment[3],
}

@ubot.on_message(filters.me & filters.command("payment", PREFIXES))
async def _(client, message):
    if len(message.command) < 2:
        x = await client.get_inline_bot_results(bot.me.username, "user_payment_command")
        try:
            return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            return await message.reply(error)
    else:
        if message.command[1] in payment_text:
            return await message.reply(payment_text[message.command[1]])
            
@bot.on_inline_query(filters.regex("^user_payment_command"))
async def _(client, inline_query):
    button = [
        [
            InlineKeyboardButton("Dana", callback_data="payment paymont"),
            InlineKeyboardButton("Bca", callback_data="payment payment"),
             ],    
        [
            InlineKeyboardButton("Gopay", callback_data="payment paymint"),
            InlineKeyboardButton("Qris", callback_data="payment paymunt"),
             ],
        ]               
msg = "<b>INI PAYMENT KENBO\nSUPPORT BY SEEKUT CORP</b>"
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Payment!",
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
                [InlineKeyboardButton("• KEMBALI •", callback_data="payment payment_back")]
            ]
            if data == "paymont":
                msg = help_payment[0]
            if data == "payment":
                msg = help_payment[1]
            if data == "paymint":
                msg = help_payment[2]
            if data == "paymunt":
                msg = help_payment[3]               
            if data == "payment_back":
               
                        button = [
                    [
                        InlineKeyboardButton(
                            "Dana", callback_data="payment paymont"
                        ),
                        InlineKeyboardButton(
                            "Bca", callback_data="payment payment"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "Gopay", callback_data="payment paymint"
                        ),
                        InlineKeyboardButton(
                            "Qris", callback_data="payment paymunt"
                        ),
                    ],                  
                ]  
                msg = "<b>HELP MENU OPEN\nSUPPORT BY SEEKUT CORP: <code>. , : ; !</code></b>"
            await callback_query.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(button)
              
            )