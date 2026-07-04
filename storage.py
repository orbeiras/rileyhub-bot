"""
storage.py
----------------------------------------
Responsável por salvar as sugestões no CSV.
"""

import csv
from datetime import datetime

from config import (
    CSV_FILE,
    CSV_HEADERS,
    DATE_FORMAT,
)


def initialize_csv():
    """
    Cria o arquivo CSV caso ele ainda não exista.
    """

    if CSV_FILE.exists():
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)


def save_suggestion()
    username,
    suggestion_type,
    project,
    category,
    character,
    actor,
    notes,
):
    """
    Salva uma sugestão no arquivo CSV.
    """

    initialize_csv()

    with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                datetime.now().strftime(DATE_FORMAT),
                username,
                suggestion_type,
                project,
                category,
                character,
                actor,
                notes,
            ]
        )
