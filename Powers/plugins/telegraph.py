import os
from telegraph import upload_file
from pyrogram import  filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


DOWNLOAD_LOCATION = "./TELEGRAPHDOWNLOADS/"

@Gojo.on_message(filters.command(["tgm"]))
async def getmedia(Gojo, update):

    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)

    try:
        message = await update.reply_text(
            text="`Processing...`",
            quote=True,
            disable_web_page_preview=True
        )
        await Gojo.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        text=f"Error :- <code>{error}</code>"
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
        )
        return

    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**"
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
            ],
        ]
    )

    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )