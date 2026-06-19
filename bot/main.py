import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# PON AQUÍ TU ID DE TELEGRAM
IDS_AUTORIZADOS = [12345678[5992488770] # Reemplaza 123456789 por tu ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no autorizado")
        return

    user = update.effective_user
    texto = f"""✅ **Usuario autorizado**

**Nombre:** {user.first_name} {user.last_name or ''}
**Username:** @{user.username or 'Sin username'}
**ID:** `{user.id}`
**Chat ID:** `{update.effective_chat.id}`
"""
    await update.message.reply_text(texto, parse_mode="Markdown")

async def cuentas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in IDS_AUTORIZADOS:
        await update.message.reply_text("❌ Usuario no autorizado")
        return

    # Aquí pones las cuentas que quieras mostrar
    texto = """📋 **Cuentas disponibles:**

1. Cuenta Premium - Activa
2. Cuenta Free - Expiró
3. Cuenta Test - Activa
"""
    await update.message.reply_text(texto, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cuentas", cuentas))
    print("Bot iniciado")
    app.run_polling()

if __name__ == "__main__":
    app.run_polling()
