# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "")
