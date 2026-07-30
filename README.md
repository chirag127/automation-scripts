# automation-scripts

[![Stars](https://img.shields.io/github/stars/chirag127/automation-scripts?style=flat-square)](https://github.com/chirag127/automation-scripts)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

Personal collection of one-off automation and scraping scripts — AdGuard filter tooling, Chrome Web Store, Discord/Telegram bots, AI-API clients, web scraping. Secrets managed via sops+age.

Large output assets (PDFs, screenshots, scraped text) are in [Releases](https://github.com/chirag127/automation-scripts/releases/tag/assets-v1).

---

## Categories

| Folder | What it does | Env vars needed |
|---|---|---|
| `adguard/` | Submit AdGuard filter issues, auto-add custom filters, AdGuard issue reporters | — |
| `chrome-store/` | Scrape Chrome Web Store extension update dates | — |
| `social/discord/` | Discord math bot, Discord prompt sender | `DISCORD_BOT_TOKEN` |
| `social/telegram/` | Telegram bot (placeholder) | — |
| `social/subscribe/` | Auto-subscribe AdGuard filter lists | — |
| `social/takeout/` | Automate Google Takeout export | — |
| `ai-apis/api_hf/` | HuggingFace Bloom/InCoder API clients, OpenAI completion helper, Bing+SayHello search | `BING_API_KEY`, `OPENAI_API_KEY` |
| `ai-apis/chatgpt/` | ChatGPT UI prompt sender via pyautogui | — |
| `ai-apis/forefront/` | Forefront GPT-J API client | — |
| `ai-apis/openassist/` | Open-Assistant UI prompt sender | — |
| `ai-apis/bardandbing/` | Bard/Bing Discord bot prompt sender | — |
| `ai-apis/bing/` | Bing auto-search tab opener | — |
| `code-hosting/github/` | GitHub comment automation | — |
| `code-hosting/gitlab/` | GitLab screenshot reference | — |
| `deepnote/` | Automate Deepnote workspace + project creation via pyautogui | — |
| `scraping/` | Blog scraper, Pocket URL bulk-add, search_all Bing opener | `POCKET_CONSUMER_KEY`, `POCKET_ACCESS_TOKEN` |
| `misc/` | Speedtest loop, graph coloring algo, scratch utilities | — |

---

## Secrets setup

All secrets are managed via **sops + age**. One shared age keypair covers all repos.

```sh
# Decrypt (requires private key at ~/.config/sops/age/keys.txt)
sops -d .env.enc > .env

# Re-encrypt after editing .env
sops --encrypt --input-type dotenv --output-type dotenv .env > .env.enc
```

Copy `.env.example` to `.env` and fill in your values. See `.env.example` for all keys and what they are for.

The age public recipient is `age1c40qjamejzrp9cajle9g0dss25mmsmyaq6uaa2pgmyr3pflsy4qspgw5c4`. Private key is in Bitwarden.

---

## License

MIT
