import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")
IDS = [5992488770] # tu ID

async def start(update, context):
    if update.effective_user.id not in IDS:
        await update.message.reply_text("❌ Usuario no registrado")
        return
    await update.message.reply_text("✅ Autorizado")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
