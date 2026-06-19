import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("Arrancando bot...")

TOKEN = os.getenv("BOT_TOKEN", "").strip()

if not TOKEN:
    print("ERROR: BOT_TOKEN vacío o no existe en Variables")
    print("Ve a Railway > Variables > crea BOT_TOKEN con tu token")
    exit(1)

print(f"Token cargado: {TOKEN[:10]}...OK")

IDS_AUTORIZADOS = [3992448770]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return
    await update.message.reply_text(f"✅ Autorizado\nID: `{update.effective_user.id}`", parse_mode="Markdown")

async def cuentas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return
    await update.message.reply_text("📋 Cuentas:\n1. Premium - Activa")

try:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cuentas", cuentas))
    print("Bot iniciado OK - esperando mensajes")
    app.run_polling()
except Exception as e:
    print(f"ERROR AL INICIAR: {e}")
    exit(1)
