from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Logging para evitar quebra de execução em erros
logging.basicConfig(level=logging.INFO)

TOKEN = "8511770355:AAF3pMBihtL2MSdeTz6Z8KdQgHcIfZx0ww0"  # ⚠️ substitua seu token aqui

link_pagamento_unico = "https://pay.cakto.com.br/zngtq6q_676932"
link_assinatura_plus = "https://pay.cakto.com.br/3aec7u6_676933"

def start(update, context):
    if update.message:
        update.message.reply_text("""
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
    else:
        update.callback_query.message.reply_text(
            """
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

def pagamento(update, context):
    keyboard = [
        [
            InlineKeyboardButton("💳 Pagamento Único", callback_data="unico"),
            InlineKeyboardButton("⭐ Assinatura Plus Mensal", callback_data="plus")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        update.message.reply_text("Qual forma de pagamento deseja?", reply_markup=reply_markup)
    else:
        update.callback_query.message.reply_text("Qual forma de pagamento deseja?", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "unico":
        query.edit_message_text(f"🔗 Pagamento Único:\n{link_pagamento_unico}")
    elif query.data == "plus":
        query.edit_message_text(f"⭐ Assinatura Plus Mensal:\n{link_assinatura_plus}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pagamento", pagamento))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
