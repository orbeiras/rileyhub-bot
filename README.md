# rileyhub-bot
Telegram bot for rileyhub suggestions.
# Riley HUB — Central de Sugestões

Bot oficial da **Riley HUB** para receber sugestões da comunidade através do Telegram.

## Funcionalidades

- Recebe sugestões de:
  - Scenepacks
  - Packs de Stickers
  - Packs de Emojis
  - Divisórias

- Coleta as seguintes informações:
  - Nome do projeto
  - Categoria
  - Personagem (opcional)
  - Ator/Atriz (opcional)
  - Observações (opcional)

- Exibe um resumo antes do envio.

- Salva todas as sugestões em um arquivo CSV.

---

## Estrutura do projeto

```
rileyhub-bot/
│
├── data/
│   └── .gitkeep
│
├── bot.py
├── config.py
├── constants.py
├── conversation.py
├── keyboards.py
├── storage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/rileyhub-bot.git
```

Entre na pasta:

```bash
cd rileyhub-bot
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Variáveis de ambiente

Crie um arquivo `.env` com:

```env
TELEGRAM_BOT_TOKEN=SEU_TOKEN_DO_BOTFATHER
```

No Railway, adicione a mesma variável em:

**Variables → New Variable**

```
TELEGRAM_BOT_TOKEN
```

---

## Executando localmente

```bash
python bot.py
```

---

## Estrutura do CSV

As sugestões são salvas em:

```
data/sugestoes.csv
```

Colunas:

- Data
- Usuário
- Tipo
- Projeto
- Categoria
- Personagem
- Ator/Atriz
- Observações

---

## Licença

Projeto desenvolvido para a comunidade **Riley HUB**.
