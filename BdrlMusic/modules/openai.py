import asyncio
import io
import random

import openai
import requests
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

from BdrlMusic import ubot
from config import OPENAI_API_KEY, PREFIXES

__MODULE__ = "OPENAI"
__HELP__ = f"""
Perintah:
          <code>{PREFIXES[0]}ai</code> or <code>{PREFIXES[0]}ask</code> [query]
Penjelasan:
           Untuk mengajukan pertanyaan ke AI

Perintah:
          <code>{PREFIXES[0]}img</code> or <code>{PREFIXES[0]}photo</code> [query]
Penjelasan:
           Untuk membuat sebuah photo 

Perintah:
          <code>{PREFIXES[0]}bing</code> or <code>{PREFIXES[0]}pic</code> [query]
Penjelasan:
           Untuk mencari photo random dari google 
"""


def openAiBot(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    json_data = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 200,
        "temperature": 0,
    }
    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, json=json_data
    ).json()
    return response["choices"][0]["text"]


def openAiText(question):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Q: {question}\nA:",
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text


def openAiPhoto(question):
    openai.api_key = OPENAI_API_KEY
    response = openai.Image.create(prompt=question, n=1, size="1024x1024")
    return response["data"][0]["url"]


@ubot.on_message(filters.me & filters.command(["ai", "ask"], PREFIXES))
async def _(client, message):
    Tm = await message.reply("<code>Memproses...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [pertanyaan]</b>")
    try:
        response = openAiText(message.text.split(None, 1)[1])
        if int(len(str(response))) > 4096:
            with io.BytesIO(str.encode(str(response))) as out_file:
                out_file.name = "openAi.txt"
                await message.reply_document(
                    document=out_file,
                )
                return await Tm.delete()
        else:
            msg = message.reply_to_message or message
            await client.send_message(
                message.chat.id, response, reply_to_message_id=msg.id
            )
            return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()


@ubot.on_message(filters.me & filters.command(["img", "photo"], PREFIXES))
async def _(client, message):
    Tm = await message.reply("<code>Memproses...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [query]</b>")
    try:
        response = openAiPhoto(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()


@ubot.on_message(filters.me & filters.command(["bing", "pic"], PREFIXES))
async def _(client, message):
    TM = await message.reply("<b>Memproses...</b>")
    if len(message.command) < 2:
        return await TM.edit(f"<code>{message.text}</code> [query]")
    x = await client.get_inline_bot_results(
        message.command[0], message.text.split(None, 1)[1]
    )
    get_media = []
    for X in range(5):
        try:
            saved = await client.send_inline_bot_result(
                client.me.id, x.query_id, x.results[random.choice(range(30))].id
            )
            saved = await client.get_messages(
                client.me.id, int(saved.updates[1].message.id)
            )
            get_media.append(InputMediaPhoto(saved.photo.file_id))
            await asyncio.sleep(1.5)
            await saved.delete()
        except:
            await TM.edit(f"<b>❌ Image Photo Ke {X} Tidak Ditemukan</b>")
    await client.send_media_group(
        message.chat.id,
        get_media,
        reply_to_message_id=message.id,
    )
    await TM.delete()
