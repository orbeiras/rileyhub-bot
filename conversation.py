"""
conversation.py
----------------------------------------------------
Fluxo principal da conversa da Central de Sugestões.
"""

from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from constants import (
    MENU,
    PROJECT,
    CATEGORY,
    CHARACTER,
    ACTOR,
    NOTES,
    CONFIRM,
    WELCOME_TEXT,
    ASK_PROJECT,
    SUGGESTION_LABELS,
)

from keyboards import build_main_menu


# ==========================================================
# /start
# ==========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Inicia o bot e exibe o menu principal.
    """

    context.user_data.clear()

    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=build_main_menu(),
    )

    return MENU


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

async def menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    suggestion_type = query.data

    context.user_data["suggestion_type"] = suggestion_type
    context.user_data["suggestion_label"] = (
        SUGGESTION_LABELS[suggestion_type]
    )

    await query.edit_message_text(
        f"Você selecionou:\n\n"
        f"{SUGGESTION_LABELS[suggestion_type]}\n\n"
        f"{ASK_PROJECT}"
    )

    return PROJECT


# ==========================================================
# CANCELAR
# ==========================================================

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    await update.message.reply_text(
        "Solicitação cancelada."
    )

    return ConversationHandler.END
  from constants import (
    ASK_CATEGORY,
    ASK_CHARACTER,
    ASK_ACTOR,
    ASK_NOTES,
)

# ==========================================================
# NOME DO PROJETO
# ==========================================================

async def ask_category(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["project"] = update.message.text.strip()

    await update.message.reply_text(
        ASK_CATEGORY
    )

    return CATEGORY


# ==========================================================
# CATEGORIA
# ==========================================================

async def ask_character(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["category"] = update.message.text.strip()

    await update.message.reply_text(
        ASK_CHARACTER
    )

    return CHARACTER


# ==========================================================
# PERSONAGEM
# ==========================================================

async def ask_actor(update: Update, context: ContextTypes.DEFAULT_TYPE):

    character = update.message.text.strip()

    if character == "-":
        character = ""

    context.user_data["character"] = character

    await update.message.reply_text(
        ASK_ACTOR
    )

    return ACTOR


# ==========================================================
# ATOR / ATRIZ
# ==========================================================

async def ask_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    actor = update.message.text.strip()

    if actor == "-":
        actor = ""

    context.user_data["actor"] = actor

    await update.message.reply_text(
        ASK_NOTES
    )

    return NOTES
  from constants import (
    SUMMARY_TITLE,
    SUCCESS_MESSAGE,
    CANCEL_MESSAGE,
    CONFIRM_CALLBACK,
    CANCEL_CALLBACK,
)

from keyboards import build_confirmation_keyboard
from storage import save_suggestion


# ==========================================================
# OBSERVAÇÕES
# ==========================================================

async def show_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):

    notes = update.message.text.strip()

    if notes == "-":
        notes = ""

    context.user_data["notes"] = notes

    summary = (
        f"{SUMMARY_TITLE}\n\n"
        f"Tipo: {context.user_data['suggestion_label']}\n"
        f"Projeto: {context.user_data['project']}\n"
        f"Categoria: {context.user_data['category']}\n"
        f"Personagem: {context.user_data['character'] or '-'}\n"
        f"Ator/Atriz: {context.user_data['actor'] or '-'}\n"
        f"Observações: {context.user_data['notes'] or '-'}"
    )

    await update.message.reply_text(
        summary,
        reply_markup=build_confirmation_keyboard(),
    )

    return CONFIRM


# ==========================================================
# CONFIRMAÇÃO
# ==========================================================

async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == CANCEL_CALLBACK:

        context.user_data.clear()

        await query.edit_message_text(
            CANCEL_MESSAGE
        )

        return ConversationHandler.END

    user = query.from_user

    username = (
        f"@{user.username}"
        if user.username
        else user.full_name
    )

    save_suggestion(
        username=username,
        suggestion_type=context.user_data["suggestion_label"],
        project=context.user_data["project"],
        category=context.user_data["category"],
        character=context.user_data["character"],
        actor=context.user_data["actor"],
        notes=context.user_data["notes"],
    )

    await query.edit_message_text(
        SUCCESS_MESSAGE
    )

    context.user_data.clear()

    return ConversationHandler.END


# ==========================================================
# CONVERSATION HANDLER
# ==========================================================

def build_conversation_handler():

    return ConversationHandler(

        entry_points=[
            CommandHandler(
                "start",
                start,
            )
        ],

        states={

            MENU: [
                CallbackQueryHandler(
                    menu_choice
                )
            ],

            PROJECT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    ask_category,
                )
            ],

            CATEGORY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    ask_character,
                )
            ],

            CHARACTER: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    ask_actor,
                )
            ],

            ACTOR: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    ask_notes,
                )
            ],

            NOTES: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    show_summary,
                )
            ],

            CONFIRM: [
                CallbackQueryHandler(
                    confirm,
                    pattern=f"^({CONFIRM_CALLBACK}|{CANCEL_CALLBACK})$",
                )
            ],

        },

        fallbacks=[
            CommandHandler(
                "cancel",
                cancel,
            )
        ],
    )
