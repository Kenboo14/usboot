from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "20063728"))
API_HASH = getenv("API_HASH", "5637eeb1cff492b89b15a1802ca99847")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", True)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001675452200]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001675452200").split()}
BOT_TOKEN = getenv("BOT_TOKEN", "6263702391:AAGXOIwMEN-I3aa9PBtvIQcli78Zer9oFEo")
SESSION_STRING = getenv("SESSION_STRING", "BQAhIHQAqJ7fKAzTTMv6Tx_yD-JvRMvizTj7OQZeCd528GCqhbZRjFuOatGfiPgKwFOIyFjIyh6CTwSiYwQH6dmwIX545JrhQdRABuJx5Irwn1x6cysF8-0uWLPJMxmVNa0gXN6qn4ke-TiWi8tXcv7-qfOCbMQd3rH9781Syg2tcT-oqSLgpEmUxdxlRO4tLAfiFBCYROk3yr7XtTyDn1RWwBYBp2QobYH7ODt89on_9ExuHOaIY-ZzGcK9aTb76ZLuh-eYmFpZPPSonzOqI5_ggSvlXJPE-91AQluN3QEh5ro4eFKjklFWJYnW5PkTkgsmgLcQj7E3gRmKYWqFgl_W-TlzKwAAAABzYhB3AA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://met:met@cluster0.zrjdoul.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1935806583").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
REPO_URL = getenv("REPO_URL", "https://github.com/Kenboo14/usboot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1935806583").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", ""
)
