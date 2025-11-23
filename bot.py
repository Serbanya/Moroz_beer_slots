import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIGURATION ---
# Replace with your Token from BotFather
TOKEN = '8109509945:AAEVRZY7aEJ9TncsS3kxpxYhZtwe6OXVT5M'
# Replace with the URL where you host the index.html (e.g., GitHub Pages)
GAME_URL = 'https://serbanya.github.io/Moroz_beer_slots/index.html'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message with a button to open the web app."""
    keyboard = [
        [InlineKeyboardButton("Play Moroz beer slots 🎰", web_app=WebAppInfo(url=GAME_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to Moroz beer slots! 🎰\nClick the button below to start playing.",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
