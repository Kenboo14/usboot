import asyncio
import logging
import sys
import time
from datetime import datetime
from logging import *
from typing import Callable
from typing import Any, Dict

from logging.handlers import RotatingFileHandler
from aiohttp import ClientSession
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pytgcalls import PyTgCalls
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyromod import listen
from rich.logging import RichHandler
from pytgcalls import GroupCallFactory

from config import *


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


if (
    not STRING_SESSION
):
    LOGGER(__name__).error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    LOGGER(__name__).error("No API_ID Found! Exiting!")
    sys.exit()

if not API_HASH:
    LOGGER(__name__).error("No API_HASH Found! Exiting!")
    sys.exit()

if BOTLOG_CHATID:
    BOTLOG_CHATID = BOTLOG_CHATID
else:
    BOTLOG_CHATID = "me"


CMD_HELP = {}
ids = []

aiosession = ClientSession()
StartTime = time.time()

START_TIME = datetime.now()


basicConfig(
    level=INFO,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[RichHandler()],
)
console = StreamHandler()
console.setLevel(ERROR)
console.setFormatter(Formatter("%(filename)s:%(lineno)s %(levelname)s: %(message)s"))
getLogger("").addHandler(console)

bot = Client(
    name="BdrlMusicubot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)
        self.call_py = PyTgCalls(self)

    def on_message(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def pytgcalls_decorator(self):
        def decorator(func):
            for ub in self._ubot:
                if func.__name__ != "stream_end":
                    ub.call_py.on_kicked()(func)
                    ub.call_py.on_closed_voice_chat()(func)
                    ub.call_py.on_left()(func)
                else:
                    ub.call_py.on_stream_end()(func)
            return func

        return decorator

    async def start(self):
        await super().start()
        await self.call_py.start()
        if self not in self._ubot:
            self._ubot.append(self)


ubot = Ubot(
    name="ubot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins=dict(root="BdrlMusic/modules"),
)

bots = [bot for bot in [ubot] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
