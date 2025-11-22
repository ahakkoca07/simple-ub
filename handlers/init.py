from telethon import functions, types
from datetime import datetime
import os

# register bot commands from commands.txt on bot launch
async def registercommands(bot):
    # Read the commands from the file
    commands = []
    commands_file = os.path.join(os.path.dirname(__file__), '..', 'commands.txt')
    
    with open(commands_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and '=' in line:
                command, description = line.split('=', 1)
                commands.append(types.BotCommand(
                    command=command.lower(),
                    description=description
                ))
    await bot(functions.bots.SetBotCommandsRequest(
        scope=types.BotCommandScopeDefault(),
        lang_code='en',
        commands=commands
    ))

# send bot startup message to log channel
async def logstart(bot, log_channel_id):
    try:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = (
            "**#STARTED**\n"
            f"**Time:** `{now}`\n"
        )
        await bot.send_message(log_channel_id, msg)
        print("Startup message has been sent.")
    except Exception as e:
        print(f"Failed to send startup message: {e}")