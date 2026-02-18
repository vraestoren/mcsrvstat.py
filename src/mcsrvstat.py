from requests import Session

class McSrvStat:
	def __init__(self, address: str, is_bedrock: bool = False) -> None:
		self.api = "https://api.mcsrvstat.us"
		self.bedrock_api = "https://api.mcsrvstat.us/bedrock"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
			"Accept": "application/json"
		}
		self.address = address
		self.is_bedrock = is_bedrock
		self.server = self.get_server_info()

	def get_server_info(self) -> dict:
		return self.session.get(
			f"{self.bedrock_api if self.is_bedrock else self.api}/2/{self.address}").json()

	def lookup_server_icon(self) -> dict:
		return self.session.get(
			f"{self.api}/icon/{self.address}").json()

	def check_server_status(self) -> str:
		return self.session.get(
			f"{self.bedrock_api if self.is_bedrock else self.api}/simple/{self.address}").text

	def debug_server(self) -> dict:
		return self.session.get(
			f"{self.api}/debug/ping/{self.address}").json()

	def debug_bedrock_server(self) -> dict:
		return self.session.get(
			f"{self.api}/debug/bedrock/{self.address}").json()

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

	def get_server_plugins(self) -> str:
		return self.server["plugins"] if "plugins" in self.server else None

	def get_server_debug(self) -> str:
		return self.server["debug"]

	def get_online_players(self) -> int:
		return self.server["players"]["online"]

	def get_max_players(self) -> int:
		return self.server["players"]["max"]

	def get_server_version(self) -> int:
		return self.server["version"]

	def get_server_ip(self) -> str:
		return self.server["ip"]

	def get_server_hostname(self) -> str:
		return self.server["hostname"]

	def get_server_protocol(self) -> int:
		return self.server["protocol"]

	def get_server_software(self) -> str:
		return self.server["software"] if "software" in self.server else None

	def get_server_id(self) -> str:
		return self.server["serverid"] if "serverid" in self.server else None

	def get_server_gamemode(self) -> str:
		return self.server["gamemode"] if "gamemode" in self.server else None
