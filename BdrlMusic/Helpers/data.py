from config import PREFIXES


class Data:
    text_help_menu = (
        f"**Command List & Help**\n**— Prefixes:** `{PREFIXES}`".replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
