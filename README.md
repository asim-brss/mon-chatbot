# Chatbot IA Local

Assistant pédagogique en informatique qui tourne entièrement en local, sans API externe ni coût.

## Aperçu

Ce chatbot utilise un modèle de langage local via LM Studio pour répondre à des questions sur l'informatique, destiné aux lycéens et étudiants en L1.

## Technologies utilisées

- Python 3.10+
- LM Studio (serveur local)
- OpenAI Python SDK (pour communiquer avec le serveur local)
- Modèle : Qwen / Gemma (au choix)

## Installation

### Prérequis
- [Python 3.10+](https://www.python.org/)
- [LM Studio](https://lmstudio.ai/) avec Qwen ou Gemma installé

### Étapes

1. Clone le repo

git clone https://github.com/asim-brss/mon-chatbot.git
cd mon-chatbot

2. Installe les dépendances

pip install -r requirements.txt


3. Lance LM Studio
   - Charge un modèle (Qwen ou Gemma)
   - Va dans l'onglet **Local Server**
   - Clique sur **Start Server**

4. Lance le chatbot
python3 chatbot.py

## Fonctionnalités

- Conversation continue avec mémoire de l'historique
- Tourne 100% en local, aucune donnée envoyée sur internet
- Aucun coût, aucune clé API requise
- Thématique pédagogique en informatique
