import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "3334521"))
    API_HASH = os.environ.get("API_HASH", "29edd7420d528140c7a04bd47486886f")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5638811601:AAEFjbHf8VzVx_0dBokFBJvu9amMKxKrVdE")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5079629749")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aryan6969:Aryan6969@cluster0.krhmwhe.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAJ9ioHaoLF5UlpXiqshagDhhOTkp8Eeyny0f8Ngi3U-tQxk35D0Ix6QD5yqZ-yJP-5OV7j0gnn6uHeKwmdRzXC1RoTEJPWYWfpRafgOi57Dadqt2xP6RglvLvBapZQPF1lO0-LoT3xVr4GRNc7Yv0BSsSkJNKUk1VZ2BelyXbCpphETdHc4imkwVXCE5AJbByshOKdp6YIWlw7dIIjIp3mBoiWlU0hHY1tGPzTUTLL6saPqLRImVCnwKWqhWfVCuaxWw6a4PvvvzkH5OjI6KT3MnpU8myZHhiI8V5-92Mw_AclV-0Iw0S5xy-GS6JZX7NrqMSEkfsJuqj23QVBC1PCY6AitAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001802577032"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@AryGiveaway_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
