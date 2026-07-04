"""
Botões (Inline Keyboards) do bot da Riley HUB.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import (
    SUGGESTION_TYPES,
    CONFIRM_CALLBACK,
    CANCEL_CALLBACK,
)


def build_main_menu() -> InlineKeyboardMarkup:
    """Cria o menu principal."""

    keyboard = [
        [InlineKeyboardButton(label, callback_data=callback)]
        for callback, label in SUGGESTION_TYPES
    ]

    return InlineKeyboardMarkup(keyboard)


def build_confirmation_keyboard() -> InlineKeyboardMarkup:
    """Botões de confirmação."""

    keyboard = [
        [
            InlineKeyboardButton(
                "Confirmar",
                callback_data=CONFIRM_CALLBACK,
            ),
            InlineKeyboardButton(
                "Cancelar",
                callback_data=CANCEL_CALLBACK,
            ),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
