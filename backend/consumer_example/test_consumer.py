import atexit
import unittest

from pact import Consumer, Provider

from .main import VersionClient

pact = Consumer("Frontend").has_pact_with(Provider("BackendAPI"))
pact.start_service()
atexit.register(pact.stop_service)


class GetVersionContract(unittest.TestCase):
    def test_get_version(self):
        expected = {"version": "0.3.0"}

        (
            pact.given("Version 0.3.0 exists")
            .upon_receiving("a request for GET /api/v1/version")
            .with_request("get", "/api/v1/version")
            .will_respond_with(200, body=expected)
        )

        client = VersionClient(base_url=pact.uri)

        with pact:
            result = client.get_version()
            self.assertEqual(result, expected)
