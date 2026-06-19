import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("ERROR: No se encontró TOKEN. Ponlo en Railway Variables")
    exit(1)

IDS_AUTORIZADOS = [3992448770] # Cambia por tu ID de @userinfobot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return
    u = update.effective_user
    await update.message.reply_text(f"✅ Autorizado\nID: `{u.id}`", parse_mode="Markdown")

async def cuentas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return
    await update.message.reply_text("📋 Cuentas:\n1. Premium - Activa")

if __name__ == "__main__":
    print("Iniciando bot...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cuentas", cuentas))
    app.run_polling()
