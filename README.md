<h1>
  <img src="https://mcsrvstat.us/img/minecraft.png" width="28" style="vertical-align:middle;" />
  mcsrvstat.py
</h1>

> Web-API for [mcsrvstat.us](https://mcsrvstat.us) to retrieve Minecraft server status, player counts, version info, plugins, and more via a simple Python interface. Supports both Java and Bedrock editions.

## Quick Start
```python
from mcsrvstat import McSrvStat

# Java Edition (default)
server = McSrvStat(address="hypixel.net")

# Bedrock Edition
server = McSrvStat(address="play.nethergames.org", is_bedrock=True)

# Get online players
print(server.get_online_players())
```

---

## Constructor Options
```python
McSrvStat(
    address="hypixel.net",  # server IP or hostname
    is_bedrock=False        # True for Bedrock edition servers
)
```

> On instantiation, `McSrvStat` automatically fetches and caches server info in `self.server` — no extra setup needed.

---

## Server Info

| Method | Returns | Description |
|--------|---------|-------------|
| `get_server_info()` | `dict` | Full server status object |
| `check_server_status()` | `str` | Simple online/offline status |
| `get_server_ip()` | `str` | Resolved server IP |
| `get_server_hostname()` | `str` | Server hostname |
| `get_server_version()` | `str` | Server version string |
| `get_server_protocol()` | `int` | Protocol version number |
| `get_server_software()` | `str\|None` | Server software (e.g. Paper, Spigot) |
| `get_server_id()` | `str\|None` | Server ID (Bedrock only) |
| `get_server_gamemode()` | `str\|None` | Default gamemode (Bedrock only) |
| `get_server_motd(is_raw, is_html, is_clean)` | `list` | Server MOTD in raw, HTML, or clean format |
| `get_server_plugins()` | `list\|None` | List of server plugins if exposed |
| `get_server_debug()` | `dict` | Debug info from cached response |

## Players

| Method | Returns | Description |
|--------|---------|-------------|
| `get_online_players()` | `int` | Current online player count |
| `get_max_players()` | `int` | Maximum player slots |

## Debug & Icons

| Method | Returns | Description |
|--------|---------|-------------|
| `lookup_server_icon()` | `dict` | Server icon data |
| `debug_server()` | `dict` | Live debug ping (Java) |
| `debug_bedrock_server()` | `dict` | Live debug ping (Bedrock) |

---

## Examples
```python
server = McSrvStat(address="hypixel.net")

# Player info
print(server.get_online_players())  # e.g. 45230
print(server.get_max_players())     # e.g. 200000

# Server details
print(server.get_server_version())  # e.g. "1.20.1"
print(server.get_server_software()) # e.g. "Paper"

# MOTD
print(server.get_server_motd(is_clean=True))  # clean text
print(server.get_server_motd(is_html=True))   # HTML formatted
```
