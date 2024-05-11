class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 5483829443
    sudo_users = "6407508299, 6176582997"
    GROUP_ID = -1002066178498
    TOKEN = "6901289852:AAG0TjmYhESxctAqWioblCRVW7-ORMlcGsc"
    mongo_url = "mongodb+srv://zhuofan21001:9Bpb5voEiKYcnUQm@cluster0.mibzqh9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://te.legra.ph/file/9f81d51fcc0cf0284a99f.jpg","https://te.legra.ph/file/9f81d51fcc0cf0284a99f.jpg"]
    SUPPORT_CHAT = "Dark_Support_Group"
    UPDATE_CHAT = "Dark_Support_Group"
    BOT_USERNAME = "waifuqueenriyabot"
    CHARA_CHANNEL_ID = "-1002004020165"
    api_id = 28213805
    api_hash = "8f80142dfef1a696bee7f6ab4f6ece34"

    
class Production(Config):
    LOGGER = True


class Development(Config): 
    LOGGER = True
