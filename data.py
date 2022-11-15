from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("💥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 💥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʙᴀᴄᴋ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🌷 ʙᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ 🌷", url="https://t.me/BikashGadgetsTech")],
        [
            InlineKeyboardButton("🌸 ʜᴇʟᴘ 🌸", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("💥 ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ 💥", url="https://t.me/Bgt_Chat")],
    ]

    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ɪғ ᴜ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ ᴛʜᴇɴ ᴛʀʏ,\n ᴏᴛʜᴇʀ ᴡɪsᴇ
1) ʟᴇᴀᴠᴇ ᴛʜɪs ʙᴏᴛ 🔚

ʏᴏᴜ ᴄᴀɴ ᴛʀᴜsᴛ ᴛʜᴇɴ ʏᴏᴜ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 💖
ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛʜ 🙂 sᴛʀɪɴɢ sᴇssɪᴏɴ (ᴠ2) 💥 ʟᴇᴀʀɴ ᴍᴏʀᴇ ᴛᴏ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ /help 💥🌷

ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʀᴇᴘᴏʀᴛ @BGT_CHAT or @ADITYADISCUS 

ᴜᴘᴅᴀᴛᴇs @BIKASHGADGETSTECH @ADITYASERVER
    """

    HELP = """
💥 **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** 💥

/about -  ᴀʙᴏᴜᴛ ᴛʜᴇ ʙɢᴛ sᴛʀɪɴɢ ʙᴏᴛ...      🌷
/cancel - ᴄᴀɴᴄᴇʟ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ᴘʀᴏᴄᴇss 🌷
/donate - ᴅᴏɴᴀᴛᴇ ғᴏʀ ᴍʏ ᴏᴡɴᴇʀ ʜᴀʀᴅᴡᴏʀᴋ 🌷
/help -   ғᴏʀ  ᴍᴏʀᴇ  ʙᴏᴛ  ᴄᴏᴍᴍᴀɴᴅs.....    🌷 
/generate - ɢᴇɴᴇʀᴀᴛᴇ  sᴛʀɪɴɢ  sᴇssɪᴏɴ...   🌷
/restart - ʀᴇsᴛᴀʀᴛ  ᴛʜᴇ  ʙᴏᴛ ᴀʟʟ  ᴘʀᴏᴄᴇss. 🌷
/start - sᴛᴀʀᴛ  ᴛʜᴇ  ʙɢᴛ  sᴛᴛɪɴɢ  ʙᴏᴛ....    🌷
"""

    ABOUT = """
**💥ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ💥** 

ᴛʜɪs ɪs ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ🌷. ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ ʙʏ @BgtStringBot 🌷 ᴘᴏᴡʀᴇᴅ ʙʏ @BIKASHGADGETSTECH @KAALWARE

sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/BGT_CHAT)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀs : @BIKASHHALDER @ADITYAHALDER
    """
