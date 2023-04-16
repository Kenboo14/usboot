import shlex
from asyncio import Future, get_event_loop
from functools import partial, wraps
from types import FunctionType

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.errors import PeerIdInvalid, UserNotParticipant
from pyrogram.types import Message

from BdrlMusic.utils.dbfunctions import get_afk_status
from config import OWNER_ID, SUDO_USERS


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let's assume that it's just one long message
    return list(filter(lambda x: len(x) > 0, split))


async def user_afk(filter, client: Client, message: Message):
    check = await get_afk_status()
    if check:
        return True
    else:
        return False


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)


def split_list(input_list, n):
    n = max(1, n)
    return [input_list[i : i + n] for i in range(0, len(input_list), n)]


def run_sync(func: FunctionType, *args, **kwargs) -> Future:
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


async def check_perms(message, permissions):
    try:
        user = await message.chat.get_member(message.from_user.id)
    except (UserNotParticipant, PeerIdInvalid, AttributeError):
        return False
    if user.status == ChatMemberStatus.OWNER:
        return True
    if user.user.id in OWNER_ID:
        return True
    if user.user.id in SUDO_USERS:
        return True
    if not permissions and user.status == ChatMemberStatus.ADMINISTRATOR:
        return True
    if user.status != ChatMemberStatus.ADMINISTRATOR:
        await message.reply_text(
            f"""
<b>🙏🏻 Mohon maaf {message.from_user.mention} anda bukan admin dari group {message.chat.title}

✅ Untuk menggunakan perintah <code>{message.text.split()[0]}</code> harus menjadi admin terlebih dahulqu</b>
""",
            quote=False,
        )
        return False

    missing_perms = [
        permission
        for permission in (
            [permissions] if isinstance(permissions, str) else permissions
        )
        if not getattr(user.privileges, permission)
    ]

    if not missing_perms:
        return True
    await message.reply_text(
        "Maaf, tetapi Anda tidak memiliki izin yang diperlukan untuk menjalankan perintah ini. Izin tidak ada: {permissions}".format(
            permissions=", ".join(missing_perms)
        ),
        quote=False,
    )
    return False


def require_admin(permissions):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message: Message, *args, **kwargs):
            if message.chat.type == ChatType.CHANNEL:
                return await func(client, message, *args, *kwargs)
            if (
                not message.from_user
                and message.sender_chat
                and message.sender_chat.id == message.chat.id
            ):
                return await func(client, message, *args, *kwargs)
            has_perms = await check_perms(message, permissions)
            if has_perms:
                return await func(client, message, *args, *kwargs)

        return wrapper

    return decorator
