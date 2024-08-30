import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7102635767:AAGzZZm7JFx0pR0vIfSYG5WekSzqSVlukrw")
    API_ID = int(os.environ.get("API_ID", 29684889))
    API_HASH = os.environ.get("API_HASH", "d437d6c7d22dbf3f0214c86a6511eee4")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
