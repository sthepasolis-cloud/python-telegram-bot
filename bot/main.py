import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# PEGA TU ID REAL AQUÍ - sácalo con @userinfobot
IDS_AUTORIZADOS = [3992448770]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return

    u = update.effective_user
    texto = f"""✅ Usuario autorizado

Nombre: {u.first_name}
Apellido: {u.last_name or 'No tiene'}
Username: @{u.username or 'Sin username'}
ID: `{u.id}`
"""
    await update.message.reply_text(texto, parse_mode="Markdown")

async def cuentas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no registrado")
        return

    texto = """📋 Cuentas:
1. Premium - Activa
2. Free - Expiró
"""
    await update.message.reply_text(texto, parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cuentas", cuentas))
    print("Bot iniciado sin botones")
    app.run_polling()
