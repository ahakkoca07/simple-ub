from telethon import events

def register(bot):
    @bot.on(events.NewMessage(pattern='/start'))
    async def start_handler(event):
        # if in pms
        if event.is_private:
            await event.reply(
f"""
This is a placeholder text for /start command in pm's.
""",
parse_mode="markdown")
        # if in a group
        elif event.is_group:
            await event.reply(
f"""
This is a placeholder text for /start command in groups.
""",
parse_mode="markdown")
        elif event.is_channel:
            await event.reply(
f"""
This is a placeholder text for /start command in channels.
""",
parse_mode="markdown")