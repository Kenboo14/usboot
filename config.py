from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20063728"))
API_HASH = getenv("API_HASH", "5637eeb1cff492b89b15a1802ca99847")
BOT_TOKEN = getenv("BOT_TOKEN", "6263702391:AAGXOIwMEN-I3aa9PBtvIQcli78Zer9oFEo")
SESSION_STRING = getenv("SESSION_STRING", "BQAhIHQAYfV_csDSALvckcm6Mv1An9qx1uccAAnvbIw-j5_CtpXm6uJ-YFU3l0wfT6ybSNi-HcVP6tC0MKdvwRJmxEFiwqEbXRL5TN753kZmQE2STPiSUkDA8EO4LQgpPmOyd4FQ4OxzRLGnlXmW-qJeRiZpntjsriLijAmZxRKNLgfxM1H7nmWf97weIX8PHk13ln-6piGBlWQU-TopB2wZiuuTBVlM-36CNDiFW68gE2k-USXxbtKYCNXS11oYtgZqhKzk46Ck5LVw8MIG2yS04Qa350gFZeFN0pOz4iiCzYPtaNWzUJN8I3gjzXED-VnSJkJuDhN3k-c42Wz73c9SnuIQAAAABzYhB3AA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://adob:adob@cluster0.0kjnbwd.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1935806583").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1935806583").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", "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"
)
