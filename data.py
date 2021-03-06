from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ð¥ Start Generating Session ð¥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ð  Return Home ð ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        [InlineKeyboardButton("â¨ sá´á´á´á´Êá´ â¨", url="https://t.me/CyniteOfficial")],
        [
            InlineKeyboardButton("Êá´Êá´â", callback_data="help"),
            InlineKeyboardButton("ðª á´Êá´á´á´ ðª", callback_data="about")
        ],
        [InlineKeyboardButton("ð¤á´á´á´á´á´á´sð¤", url="https://t.me/StarkBots")],]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @CyniteBots
    """

    HELP = """
â¨ **Available Commands** â¨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @cyniteBots

Source Code : [Contact](https://t.me/cyniteofficial)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @cyniteofficial
    """
