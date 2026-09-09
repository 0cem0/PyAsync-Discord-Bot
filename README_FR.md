# PyAsync Discord Bot

🇫🇷 Version Française | [🇬🇧 Read in English](README.md)

> Un bot Discord léger et 100% asynchrone en Python, démontrant l'utilisation de requêtes API non-bloquantes et la gestion de tâches simultanées.

Ce projet démontre comment créer un bot Discord en Python capable de gérer de multiples tâches en simultané sans bloquer la boucle d'événements (Event Loop) grâce à `asyncio`.

---

## Fonctionnalités

- **Architecture Asynchrone** : Conçu avec `discord.py` et `aiohttp` pour des performances optimales.
- **Réponse Automatique** : Écoute du chat et interaction basique (détection de mots-clés).
- **Minuteur Non-Bloquant** : Lancement de minuteurs en arrière-plan permettant au bot de continuer à répondre aux autres utilisateurs.
- **Tracker Crypto en Direct** : Interrogation asynchrone de l'API publique CoinGecko pour récupérer le prix en euros de n'importe quelle cryptomonnaie.

---

## Installation

1. **Installer les dépendances** :
   ```bash
   pip install discord.py aiohttp
   ```

2. **Configuration du Token** :
   - Ouvrez le fichier `bot.py`
   - Remplacez la valeur `"PLACEHOLDER"` par le token de votre bot Discord (généré sur le portail développeur Discord).

---

## Utilisation

Lancez le bot directement depuis votre terminal :

```bash
python bot.py
```

### Liste des commandes

| Commande | Exemple | Description |
| :--- | :--- | :--- |
| `!ping` | `!ping` | Renvoie la latence actuelle du bot en millisecondes. |
| `!timer` | `!timer 10` | Lance un compte à rebours asynchrone du nombre de secondes indiqué. |
| `!crypto` | `!crypto bitcoin` | Récupère et affiche le prix en temps réel de la cryptomonnaie spécifiée (en euros). |

---

## Prérequis API Discord
Assurez-vous d'avoir activé le **Message Content Intent** dans la section *Bot* du Discord Developer Portal pour que les commandes puissent être lues correctement.
