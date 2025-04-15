# 📤 Telegram Message Copier

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Telethon](https://img.shields.io/badge/Telethon-API-green?logo=telegram&logoColor=white)
![License](https://img.shields.io/github/license/rudineialves/telegram-message-copier)
![Repo Size](https://img.shields.io/github/repo-size/rudineialves/telegram-message-copier)
![Last Commit](https://img.shields.io/github/last-commit/rudineialves/telegram-message-copier)
![GitHub stars](https://img.shields.io/github/stars/rudineialves/telegram-message-copier?style=social)
![GitHub forks](https://img.shields.io/github/forks/rudineialves/telegram-message-copier?style=social)

---

Este é um script simples em **Python** que copia mensagens de um canal do Telegram para outro de forma automatizada, usando a biblioteca [Telethon](https://github.com/LonamiWebs/Telethon).

## 🚀 Descrição

Sempre que uma nova mensagem é postada no canal de origem, ela é automaticamente enviada para o canal de destino.

## 🛠️ Tecnologias utilizadas

- Python 3
- Telethon

## 📦 Instalação

1. Clone este repositório:
```bash
  git clone https://github.com/rudineialves/telegram_message_copier.git
  cd telegram_message_copier
```

2. Instale a biblioteca necessária:

  ```bash
  pip install telethon
  ```

3. Edite o script com:

- Seu api_id e api_hash (obtenha em my.telegram.org)

- IDs dos canais de origem e destino

## 🧠 Como usar
Execute o script com:

  ```bash
  python script.py
  ```

Ele irá:

- Monitorar o canal de origem
- Copiar automaticamente as novas mensagens para o canal de destino

## ⚠️ Observações

- Não é necessário o Telegram permanecer aberto pois o script utiliza a API oficial.
- Você precisa ser administrador do canal destino.
- O script só envia mensagens de texto.
- Esse código é uma base simples e pode ser expandido para lidar com mídias, filtros, logs, etc.

## 📄 Licença
Este projeto é open source e está sob a licença MIT.

💻 Feito por [Rudinei Alves](https://www.linkedin.com/in/rudinei-alves/)
