# Telethon Core

A modular Telegram bot framework built with [Telethon](https://github.com/LonamiWebs/Telethon).

## Features

- **Highly Modular**: Only write your modules and drop them in the `handlers/` folder
- **Docker Support**: Because who doesn't like Docker?

This framework is really basic for easy development, so i haven't added much modules by default.

## Requirements

- Python 3.11 or higher
- Telegram API credentials (API ID and API Hash)
- Telegram Bot Token from [@BotFather](https://t.me/botfather)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/ahakkoca07/telethon-core.git
cd telethon-core
```

2. Create a `.env` file with your credentials:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
DATA_FOLDER=./data
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/ahakkoca07/telethon-core.git
cd telethon-core
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials (see [Configuration](#configuration))

4. Run the bot:
```bash
python3 main.py
```

## Configuration

Create a `.env` file in the root directory with the following variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) | Yes |
| `API_HASH` | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | Yes |
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/botfather) | Yes |
| `DATA_FOLDER` | Directory for storing bot session and data (default: `./data`) | Yes |
| `SUDO_USERS` | Comma-separated list of admin IDs | No |
| `LOG_CHANNEL_ID` | Channel ID for logging | No |

## Project Structure

```
telethon-core/
├── main.py                 # the main bot
├── requirements.txt        # py dependencies
├── Dockerfile             # docker image building
├── docker-compose.yml     # docker compose
├── .env                   # environment vars
├── data/                  # bot session and permanent data for handlers
└── handlers/              # handlers directory
    ├── init.py           # boot logging and command registering
    ├── start.py          # /start handler
    ├── help.py           # /help handler
    └── addchat.py        # adding to chat handler
```

## Creating Custom Handlers

To add a new command handler, create a Python file in the `handlers/` directory:

```python
from telethon import events

def register(bot):
    @bot.on(events.NewMessage(pattern='/command'))
    async def command_handler(event):
        if event.is_private:
            await event.reply("Response in private chats")
        elif event.is_group:
            await event.reply("Response in groups")
        elif event.is_channel:
            await event.reply("Response in channels")
```
The bot will automatically load and register your handler on startup.

> **Note**: Optionally you can add it to `commands.txt` too.

## Available Commands

- `/start` - Start the bot (shows different messages in PMs, groups, and channels)
- `/help` - Display help information (context-aware responses)

## Development

### Adding New Features

1. Create a new handler file in the `handlers/` directory
2. Implement the `register(bot)` function
3. Use Telethon's event system to handle messages or events
4. The handler will be automatically loaded on bot restart

### Debugging

Check Docker logs:
```bash
docker-compose logs -f
```

Or run directly to see output:
```bash
python3 main.py
```

## Docker Commands

```bash
# Start the bot
docker compose up -d

# Stop the bot
docker compose down

# View logs
docker compose logs -f
```

## Security Notes

- Keep your API id and hash secure
- Make sure to add rate limiting and proper logging when using this core

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Commit your changes (`git commit -m 'Added rate limiting'`)
3. Push to the branch (`git push`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Telethon documentation](https://docs.telethon.dev/)

---

**Note**: This is a core framework. Command handlers use placeholder messages that should be customized.
