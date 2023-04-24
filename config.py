from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20063728"))
API_HASH = getenv("API_HASH", "5637eeb1cff492b89b15a1802ca99847")
BOT_TOKEN = getenv("BOT_TOKEN", "6263702391:AAGXOIwMEN-I3aa9PBtvIQcli78Zer9oFEo")
SESSION_STRING = getenv("SESSION_STRING", "BQAhIHQAEa7LkWYujzbF5WB5J2WLkLm1wC4YEpvSpUTbr9mGXjN3DpBJrwhZJb0pE68wcqmvgqWPuhaFLsFrqkC0ZmBYEJGVUue4GY6PUZldB5kuCehD5zAHdKceYwHBibPD4Dfn7Kt0AnOuhw25yjSbLHwCaw-ht59yOcS5RbjvegcGC8qAmlQczXQCYfgJRqK3buiZif9IgHWt_UfyfsrNTpEBS1BjesQPvbUcshew0NcxZ7KFA3MEX1I3f8FtSyAAykfQkcO2vbS02F3aFbx0MmeS_aqS7ypUVHupvDWO5MN_5vGtphyPd7xuD6IcfG6gMOQo8tQSbFw4SobUWcOJHjmyfgAAAABzYhB3AA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://adob:adob@cluster0.0kjnbwd.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1935806583").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1935806583").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", "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"
)
