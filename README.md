# mcsrvstat.py
Web-API for [mcsrvstat](https://mcsrvstat.us) an Minecraft Server Status API that provides a comprehensive service which combines the Ping and Query protocols to deliver server status information in JSON format. The API is designed to offer a simplified way to retrieve information about Minecraft servers, including details such as player count, server version, plugins, and more.

## Example
```python
import mcsrvstat
mcsrvstat = mcsrvstat.McSrvStat(address="", is_bedrock=False)
online_players = mcsrvstat,get_online_players()
print(online_players)
```
