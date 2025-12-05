import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Logging para evitar quebra de execução em erros
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

link_pagamento_unico = "https://pay.cakto.com.br/zngtq6q_676932"
link_assinatura_plus = "https://pay.cakto.com.br/3aec7u6_676933"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = ("""
            "📺✨ Bem-vindo(a) ao seu canal de Doramas e Séries Asiáticas! ✨🎬

Aqui você encontra novelas, k-dramas, c-dramas, j-dramas e muito mais, com acesso fácil e atualizado! 💖

Escolha como quer aproveitar todo esse conteúdo:

💳 Acesso 7 dias — Pagamento Único
➡️ Assista tudo por apenas R$ 11,99

⭐ Assinatura Plus Mensal
➡️ Tenha acesso contínuo por R$ 5,99/mês
                                  
👉 Toque em /pagamento e selecione a opção ideal para você!

OBS: Você receberá o link para o grupo POR EMAIL após confirmação do pagamento.

Prepare a pipoca e vamos maratonar juntos! 🍿🔥"""
    )
    await update.message.reply_text(mensagem, parse_mode="Markdown")

async def pagamento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💳 Pagamento Único", callback_data="unico"),
            InlineKeyboardButton("⭐ Assinatura Plus Mensal", callback_data="plus")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Qual forma de pagamento deseja?", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "unico":
        await query.edit_message_text(f"🔗 Pagamento Único:\n{link_pagamento_unico}")
    elif query.data == "plus":
        await query.edit_message_text(f"⭐ Assinatura Plus Mensal:\n{link_assinatura_plus}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pagamento", pagamento))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot iniciado!")
    app.run_polling()

if __name__ == "__main__":
    main()

