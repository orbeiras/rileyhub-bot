"""
Configurações do bot da Riley HUB.
"""

import os
from pathlib import Path

# ==========================================
# TOKEN DO TELEGRAM
# ==========================================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
   raise RuntimeError(
    "A variável de ambiente TELEGRAM_BOT_TOKEN não foi encontrada. "
    "Configure-a no Railway (Variables) ou no arquivo .env."
)

# ==========================================
# INFORMAÇÕES DO BOT
# ==========================================

BOT_NAME = "Central de Sugestões"

# ==========================================
# PASTAS
# ==========================================

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILE = DATA_DIR / "sugestoes.csv"

# ==========================================
# CSV
# ==========================================

CSV_HEADERS = [
    "Data",
    "Usuário",
    "Tipo",
    "Projeto",
    "Categoria",
    "Personagem",
    "Ator/Atriz",
    "Observações",
]

# ==========================================
# CONFIGURAÇÕES GERAIS
# ==========================================

DATE_FORMAT = "%d/%m/%Y %H:%M"

SKIP = "-"
