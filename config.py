from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001675452200]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_STRING = getenv("SESSION_STRING", "")
MONGO_URL = getenv("MONGO_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "c41d3ad7-4dfd-45b1-be88-053a05704b56")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "testetstesh")
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
REPO_URL = getenv("REPO_URL", "https://github.com/Kenboo14/usboot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", ""
)
