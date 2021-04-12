import os
from instagram_bot import InstaBot

SIMILAR_ACCOUNT = "anaissinh"
IG_USER = os.getenv('IG_USER')
IG_PASSWORD = os.getenv('IG_PASSWORD')
IG_URL = "https://www.instagram.com/accounts/login/"

# Create Bot Object
bot = InstaBot()

# Login to IG
bot.login(ig_url=IG_URL, ig_user=IG_USER, ig_pwd=IG_PASSWORD)

# Access to the similar account
bot.find_followers(similar_account=SIMILAR_ACCOUNT)

# Follow all their followers
bot.follow()
