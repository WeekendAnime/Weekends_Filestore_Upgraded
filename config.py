#(©)Anime_Weekends




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7378354734:AAGb8dZm_Ref8Ln3brARcwrllIkZwWgJMhM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28744454"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002437344784"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6266529037"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://drapixstore:Y7DJWJCCpBQClI5o@cluster0.fq7ee6x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002076655534"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002369384920"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002172787340"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002244170363"))

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "600"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/ALf.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/Gsx.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴋᴏɴɪᴄʜɪᴡᴀ {mention}\n\nᴋᴏɴɪᴄʜɪᴡᴀ ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴀɴɪᴍᴇ/ᴍᴏᴠɪᴇ ғɪʟᴇs ɪɴ @Anime_Weekends ᴄʜᴀɴɴᴇʟ  ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6429532957 6266529037").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE", 
    "ᴀʀᴀ ᴀʀᴀ!! {mention}\n\n<b> sᴏ ᴡʜᴀᴛ’s ᴡʀᴏɴɢ ᴡɪᴛʜ ᴛʜᴀᴛ? ɪ ʙᴇᴄᴀᴍᴇ ᴛʜᴇ sᴛᴜᴅᴇɴᴛ ᴄᴏᴜɴᴄɪʟ ᴘʀᴇsɪᴅᴇɴᴛ ᴛᴏ ᴡɪɴ ᴛʜᴇ ʜᴇᴀʀᴛ ᴏғ ᴛʜᴇ ɢɪʀʟ ɪ ʟᴏᴠᴇ. ᴀ ʀᴇᴀsᴏɴ ғᴀʀ ᴍᴏʀᴇ ɪᴍᴘʀᴏᴘᴇʀ ᴛʜᴀɴ ᴀɴʏ ʏᴏᴜ ᴍᴀʏ ʜᴀᴠᴇ.\n\nKindly ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ</b>"
)

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @Ongoing_Weekends</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ᴀʀᴀ!! ᴀʀᴀ!! ɪᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴍʏ ʟᴏᴠᴇʟʏ ᴋᴀᴡᴀɪɪ 🥰 @JeffreySama !"

ADMINS.append(OWNER_ID)
ADMINS.append(6266529037)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
