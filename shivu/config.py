class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7526369190"
    sudo_users = "7526369190", "6961287189", "7334126640", "5920352309", "7078181502", "1414467834"
    GROUP_ID = -1002119873436
    TOKEN = "7367511450:AAFb78v-duwLXS0IZraAU33CEPxdg5SVCs0"
    mongo_url = "mongodb+srv://userbot:userbot@cluster0.iweqz.mongodb.net/test?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg"]
    SUPPORT_CHAT = "waifexanime"
    UPDATE_CHAT = "waifebot_supoort"
    BOT_USERNAME = "Collectionwaife_bot"
    BOT_NAME = "˹waife x anime˼ 🥀"
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
