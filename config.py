from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_STRING = getenv("SESSION_STRING", "")
MONGO_URL = getenv("MONGO_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", ""
)
