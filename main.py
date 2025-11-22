from telethon import TelegramClient
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Telethon stuff
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# If the bot has admin specific behaivour, set sudo users
# sudo_env = os.getenv('SUDO_USERS')

# Bot log channel id, better to have
# log_channel_id = int(os.getenv("LOG_CHANNEL_ID"))

# If bot needs to store data permanently somewhere
# data_folder = os.getenv("DATA_FOLDER")

# If the bot is using AI
# gemini_key = os.getenv("GOOGLE_API_KEY")

# read system prompt
# Load the text file
# with open(f"{data_folder}/sysprompt.txt", "r", encoding="utf-8") as f:
#    sysprompt = f.read()

# test if the system prompt is loading
# print(sysprompt)

# convert sudo users env value into a python list
# sudo_users = [int(x.strip()) for x in sudo_env.split(',')]

# Test if sudo users are parsed correctly
# print(sudo_users[])

# for i in range(len(sudo_users)):
#    print(sudo_users[i])

# init bot
bot = TelegramClient(f'{data_folder}/bot', api_id, api_hash)
bot.start(bot_token=bot_token)

# import setup utils
from handlers.init import registercommands, logstart, handlers

# import handlers and register
from handlers.start import register as register_start
register_start(bot)

from handlers.help import register as register_help
logregister(bot, log_channel_id, "help", register_help)

# from handlers.about import register as register_about
# logregister(bot, log_channel_id, "about", register_about)


if __name__ == '__main__':
    print("Starting bot...")

    async def main():
        await registercommands(bot)
# for logging bot starting
#         await logstart(bot, log_channel_id)
        await bot.run_until_disconnected()
    with bot:
        bot.loop.run_until_complete(main())
