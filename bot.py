"""
Bot principal da Riley HUB.
"""

import logging

from telegram.ext import Application

from config import BOT_TOKEN
from conversation import build_conversation_handler

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Registra toda a conversa do bot
    app.add_handler(build_conversation_handler())

    print("✅ Riley HUB Bot iniciado!")

    app.run_polling()


if __name__ == "__main__":
    main()
