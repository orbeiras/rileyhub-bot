"""
Mensagens, estados da conversa e constantes do bot.
"""

# ==========================================================
# MENSAGEM INICIAL
# ==========================================================

WELCOME_TEXT = (
    "Toda memória começa com uma ideia. Compartilhe-as conosco.\n\n"
    
)

# ==========================================================
# PERGUNTAS
# ==========================================================

ASK_PROJECT = "Qual é o nome do projeto?"

ASK_CATEGORY = (
    "Qual é a categoria?\n\n"
    "Exemplos:\n"
    "• Filme\n"
    "• Série\n"
    "• Dorama\n"
    "• Animação\n"
    "• Videoclipe"
)

ASK_CHARACTER = (
    "Qual é o personagem?\n\n"
    "Caso não queira informar, envie apenas -"
)

ASK_ACTOR = (
    "Qual é o ator ou atriz?\n\n"
    "Caso não queira informar, envie apenas -"
)

ASK_NOTES = (
    "Deseja adicionar alguma observação?\n\n"
    "Caso não queira informar, envie apenas -"
)

# ==========================================================
# MENSAGENS FINAIS
# ==========================================================

SUCCESS_MESSAGE = (
    "Sua sugestão foi enviada com sucesso!\n\n"
    "Obrigado por sonhar conosco."
)

CANCEL_MESSAGE = (
    "Solicitação cancelada.\n\n"
    "Envie /start para começar novamente."
)

SUMMARY_TITLE = "Confira sua sugestão:"

# ==========================================================
# TIPOS DE SUGESTÃO
# ==========================================================

SUGGESTION_TYPES = [
    ("scenepack", "Scenepack"),
    ("stickers", "Stickers"),
    ("emojis", "Emojis"),
    ("divisorias", "Divisórias"),
]

# ==========================================================
# CALLBACKS
# ==========================================================

CONFIRM_CALLBACK = "confirmar"
CANCEL_CALLBACK = "cancelar"

# ==========================================================
# ESTADOS DA CONVERSA
# ==========================================================

(
    MENU,
    PROJECT,
    CATEGORY,
    CHARACTER,
    ACTOR,
    NOTES,
    CONFIRM,
) = range(7)
SUGGESTION_LABELS = {
    callback: label
    for callback, label in SUGGESTION_TYPES
}
