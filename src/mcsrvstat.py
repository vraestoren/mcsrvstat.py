from requests import Session

class McSrvStat:
    def __init__(self, address: str, is_bedrock: bool = False) -> None:
        self.api = "https://api.mcsrvstat.us"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
            "Accept": "application/json"
        }
        self.address = address
        self.is_bedrock = is_bedrock
        self.server = self.get_server_info()

    def _base(self) -> str:
        return f"{self.api}/bedrock" if self.is_bedrock else self.api

    def _get(self, endpoint: str) -> dict:
        return self.session.get(f"{self.api}{endpoint}").json()

    def _get_text(self, endpoint: str) -> str:
        return self.session.get(f"{self.api}{endpoint}").text

    def get_server_info(self) -> dict:
        return self.session.get(
            f"{self._base()}/2/{self.address}").json()

    def lookup_server_icon(self) -> dict:
        return self._get(f"/icon/{self.address}")

    def check_server_status(self) -> str:
        return self.session.get(
            f"{self._base()}/simple/{self.address}").text

    def debug_server(self) -> dict:
        return self._get(f"/debug/ping/{self.address}")

    def debug_bedrock_server(self) -> dict:
        return self._get(f"/debug/bedrock/{self.address}")

    def get_server_motd(
            self,
            is_raw: bool = False,
            is_html: bool = False,
            is_clean: bool = False) -> list:
        if is_raw:
            return self.server["motd"]["raw"]
        if is_html:
            return self.server["motd"]["html"]
        if is_clean:
            return self.server["motd"]["clean"]
        return self.server["motd"]["clean"]

    def get_server_plugins(self) -> list | None:
        return self.server.get("plugins")

    def get_server_debug(self) -> dict:
        return self.server["debug"]

    def get_online_players(self) -> int:
        return self.server["players"]["online"]

    def get_max_players(self) -> int:
        return self.server["players"]["max"]

    def get_server_version(self) -> str:
        return self.server["version"]

    def get_server_ip(self) -> str:
        return self.server["ip"]

    def get_server_hostname(self) -> str:
        return self.server["hostname"]

    def get_server_protocol(self) -> int:
        return self.server["protocol"]

    def get_server_software(self) -> str | None:
        return self.server.get("software")

    def get_server_id(self) -> str | None:
        return self.server.get("serverid")

    def get_server_gamemode(self) -> str | None:
        return self.server.get("gamemode")
