#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Jҽϝϝɾҽყ ʂαɱα</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Weekends'>ᴀɴɪᴍᴇ ᴡᴇᴇᴋᴇɴᴅs</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Movie_Weekends'>ᴍᴏᴠɪᴇ ᴡᴇᴇᴋᴇɴᴅs</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Weekends_Network'>ᴡᴇᴇᴋᴇɴᴅs ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/Weebs_Weekends'>ᴡᴇᴇʙs ᴡᴇᴇᴋᴇɴᴅs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ Cℓσѕє", callback_data = "close"),
                    InlineKeyboardButton('🍁 Oωиєя', url='https://t.me/JeffreySama')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
