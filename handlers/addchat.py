from telethon import events

def register(bot):
    @bot.on(events.ChatAction)
    async def addchat_handler(event):
        bot_me = await bot.get_me()
        if (event.user_added or event.user_joined) and not event.action_message:
            if bot_me.id in event.user_ids:
                # Send welcome message based on chat type
                if event.is_group:
                    await event.reply("This is a placeholder text for when the bot is added in groups.")
                elif event.is_channel:
                    await event.reply("This is a placeholder text for when the bot is added in channels.")
