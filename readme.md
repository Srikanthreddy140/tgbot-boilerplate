# Telegram Bot Boilerplate Using Pyrogram

A simple and organized boilerplate to kickstart your Telegram bot development using [Pyrogram](https://docs.pyrogram.org/) (PyroFork).

## ✨ Features
- Clean and modular folder structure for better maintainability.
- Easy-to-use setup with essential plugins pre-configured.
- Ready-to-go bot class for faster development.
- Sample plugin with inline keyboard examples.

## 🚀 Getting Started

Follow these simple steps to set up your Telegram bot using this boilerplate:

### 1. Clone the Repository
```bash
git clone https://github.com/biisal/boilerplate.git
cd boilerplate
```
### 2. Install Dependencies

Make sure you have Python 3.9+ installed. Use pip to install the required libraries:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a .env file in the root directory and add your bot's API credentials:

```py
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
ADMIN=your_admin_user_id
```

Replace your_api_id, your_api_hash, your_bot_token, and your_admin_user_id with the actual values from Telegram BotFather and your Telegram account.
### 4. Run the Bot

Simply start your bot with:

```
python3 bot.py
```
or 

```
python bot.py
```
### 5. Test the Bot

Send /start to your bot to see it in action! The boilerplate includes a sample /start command with an inline keyboard.
🗂️ Folder Structure

Here's a quick overview of the project structure:
```
.
├── plugins/
│   ├── callback.py       # Example for handling callback queries
│   └── commands.py       # Example for handling commands like /start
├── bot.py                # Main entry point for the bot
├── db.py                 # Placeholder for database connection
├── vars.py               # Handles environment variables
├── requirements.txt      # List of dependencies
└── .env                  # (ignored) Your bot credentials
```

- plugins/: Contains modular plugins for your bot commands and functionalities.
- bot.py: Initializes the bot and sets up plugins.
- vars.py: Manages settings imported from the .env file.


📖 Example Plugin: /start

The commands.py file demonstrates how to create a simple command with an inline keyboard:
```
@Client.on_message(filters.command("start") & filters.incoming)
async def start(client: Client, message: Message):
    await message.reply_text(
        f"**Hello {message.from_user.first_name}!**\nThis boilerplate is ready to go.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Help", url="https://t.me/devdoptpy"),
                    InlineKeyboardButton("Callback ping", callback_data=f"ping#{message.from_user.id}")
                ]
            ]
        )
    )
```
This creates an inline keyboard with buttons for external links and callbacks.
- Modify bot.py to set up your bot's custom configurations.
- Add more plugins to the plugins/ folder for new commands or features.
- Use db.py to integrate your preferred database solution (e.g., MongoDB, PostgreSQL).


### 🛠️ Contributing

Feel free to fork this project and submit pull requests! Suggestions and contributions are welcome to improve this boilerplate.


Ready to build your Telegram bot? Start here!