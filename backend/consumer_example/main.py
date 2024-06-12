import requests


class VersionClient:
    def __init__(
        self,
        base_url: str = "https://example.com/api/v1",
    ):
        self.base_url = base_url

    def get_version(self) -> dict[str, str | int | list[str]]:
        return requests.get("/".join([self.base_url, "api/v1/version"])).json()
