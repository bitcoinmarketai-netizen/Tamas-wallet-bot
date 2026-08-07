# Tamas-wallet-bot
Tamas Wallet — a simple and secure Telegram-based crypto wallet platform with TON support.
import os
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📱 ورود با شماره تلفن", request_contact=True)]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        "👋 به Tamas Wallet خوش آمدید!\n\n"
        "برای شروع، شماره تلفن خود را با دکمه زیر ارسال کنید.",
        reply_markup=reply_markup
    )


async def contact_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact

    await update.message.reply_text(
        f"✅ شماره {contact.phone_number} دریافت شد.\n\n"
        "💼 کیف پول شما در مرحله بعد ایجاد خواهد شد.\n"
        "🌐 شبکه: TON Testnet\n\n"
        "⚠️ این نسخه آزمایشی است."
    )


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.CONTACT, contact_received)
    )

    print("Tamas Wallet Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
