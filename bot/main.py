   import os
   import logging
   from telegram import Update, ReplyKeyboardMarkup
   from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

   TOKEN = os.getenv("TOKEN")
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
       keyboard = [['Hola', 'Ayuda'], ['Ping']]
       reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
       await update.message.reply_text('¡Bot 24/7 activo! Elige una opción:', reply_markup=reply_markup)

   async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text('Comandos: /start - /help - /ping')

   async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text('Pong! Bot funcionando 24/7')

   async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text(f'Tú dijiste: {update.message.text}')

   if __name__ == '__main__':
       app = ApplicationBuilder().token(TOKEN).build()
       app.add_handler(CommandHandler("start", start))
       app.add_handler(CommandHandler("help", help_command))
       app.add_handler(CommandHandler("ping", ping))
       app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
       print("Bot iniciado...")
       app.run_polling()
