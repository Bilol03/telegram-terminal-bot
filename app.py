import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a terminal commands bot. Write me terminal commands!")

async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = subprocess.run(update.message.text, capture_output=True, text=True, shell=True)
    # print(result)
    # print(result.stdout)
    result = result.stdout
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    
    # print(result.stderr)
    
    
    
if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    
    start_handler = CommandHandler('start', start)
    other_commands = MessageHandler(filters.TEXT & (~filters.COMMAND), commands)
    application.add_handler(start_handler)
    application.add_handler(other_commands)
    
    application.run_polling()