class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7526369190"
    sudo_users = "7526369190", "6961287189", "7334126640", "5920352309", "7078181502", "1414467834"
    GROUP_ID = -1002214016605
    TOKEN = "6639816047:AAFwzilYfHCrnIuyBFdJZjvBJn09hfHJ_WY"
    mongo_url = "mongodb+srv://Epic2:w85NP8dEHmQxA5s7@cluster0.tttvsf9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg"]
    SUPPORT_CHAT = "Grabbing_Your_WH_Group"
    UPDATE_CHAT = "FLEX_BOTS_NEWS"
    BOT_USERNAME = "Grabbing_Your_Waifu_XBot"
    BOT_NAME = "˹𝐆ʀᴀʙʙɪɴɢ 𝐘ᴏᴜʀ 𝐖ᴀɪғᴜ˼ 🥀"
    CHARA_CHANNEL_ID = "-1002031911980"
    api_id = 24089031
    api_hash = "0615e3afe13ddaaf8e9ddbd3977d35ff"

    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
