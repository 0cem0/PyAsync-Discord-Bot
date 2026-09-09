# PyAsync Discord Bot 

[🇫🇷 Lire en Français](README_FR.md) | 🇬🇧 English Version

> A lightweight and 100% asynchronous Discord bot built with Python, showcasing non-blocking API calls and concurrent task management.

This project demonstrates how to build a Discord bot in Python capable of handling multiple operations simultaneously without blocking the Event Loop using `asyncio`.

---

## Features

- **Asynchronous Architecture**: Built with `discord.py` and `aiohttp` for optimal performance.
- **Auto-responder**: Chat listener with basic interactions (keyword detection).
- **Non-blocking Timer**: Background timers allowing the bot to keep serving other users concurrently.
- **Live Crypto Tracker**: Asynchronous integration with CoinGecko API to get real-time cryptocurrency prices in EUR.

---

## Installation

1. **Install Dependencies**:
   ```bash
   pip install discord.py aiohttp
   ```

2. **Configure Your Token**:
   - Open `bot.py`
   - Replace `"PLACEHOLDER"` with your actual Discord Bot Token from the Discord Developer Portal.

---

## Usage

Run the bot directly from your terminal:

```bash
python bot.py
```

### Available Commands

| Command | Example | Description |
| :--- | :--- | :--- |
| `!ping` | `!ping` | Returns the current bot latency in milliseconds. |
| `!timer` | `!timer 10` | Starts a non-blocking asynchronous countdown. |
| `!crypto` | `!crypto bitcoin` | Fetches and displays the real-time price of the specified crypto in EUR. |

---

## Discord API Prerequisite
Make sure to enable the **Message Content Intent** in the *Bot* section of your Discord Developer Portal.
