from enum import IntEnum, unique


@unique
class Types(IntEnum):
    TEXT = 1
    DOCUMENT = 2
    PHOTO = 3
    VIDEO = 4
    STICKER = 5
    AUDIO = 6
    VOICE = 7
    VIDEO_NOTE = 8
    ANIMATION = 9
    ANIMATED_STICKER = 10
    CONTACT = 11


def get_message_type(msg):
    if msg.text or msg.caption:
        content = None
        message_type = Types.TEXT
    elif msg.sticker:
        content = msg.sticker.file_id
        message_type = Types.STICKER

    elif msg.document:
        if msg.document.mime_type == "application/x-bad-tgsticker":
            message_type = Types.ANIMATED_STICKER
        else:
            message_type = Types.DOCUMENT
        content = msg.document.file_id

    elif msg.photo:
        content = msg.photo.file_id  # last elem = best quality
        message_type = Types.PHOTO

    elif msg.audio:
        content = msg.audio.file_id
        message_type = Types.AUDIO

    elif msg.voice:
        content = msg.voice.file_id
        message_type = Types.VOICE

    elif msg.video:
        content = msg.video.file_id
        message_type = Types.VIDEO

    elif msg.video_note:
        content = msg.video_note.file_id
        message_type = Types.VIDEO_NOTE

    elif msg.animation:
        content = msg.animation.file_id
        message_type = Types.ANIMATION

    # TODO
    # elif msg.contact:
    # 	content = msg.contact.phone_number
    # 	# text = None
    # 	message_type = Types.CONTACT

    # TODO
    # elif msg.animated_sticker:
    # 	content = msg.animation.file_id
    # 	text = None
    # 	message_type = Types.ANIMATED_STICKER

    else:
        return None, None

    return content, message_type
