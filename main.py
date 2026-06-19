from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = 117623288
AUTHORIZED_USERS = [5992488770]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USERS:
        await update.message.reply_text("❌ No autorizado")
        return
    await update.message.reply_text("✅ Autorizado. Escribe tu mensaje:")

async def private_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USERS:
        await update.message.reply_text("❌ No autorizado")
        return

    user = update.effective_user
    text = update.message.text
    username = f"@{user.username}" if user.username else "sin username"

    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=f"👤 {user.full_name} {username}\nID: {user_id}\n\n{text}"
    )
    await update.message.reply_text("✅ Enviado")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Error: {context.error}")

def main():
    if not TOKEN:
        print("ERROR: BOT_TOKEN no encontrado en variables de entorno")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, private_message))
    app.add_error_handler(error_handler)
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
