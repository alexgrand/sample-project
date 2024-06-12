import unittest

from pact import Verifier

broker_opts = {
    "broker_url": "http://localhost:9292/",
    "publish_version": "0.3.0",
    "publish_verification_results": True,
}

verifier = Verifier(provider="BackendAPI", provider_base_url="http://localhost")


class GetUserInfoContract(unittest.TestCase):
    def test_get_version(self):
        success, logs = verifier.verify_with_broker(
            **broker_opts,
            verbose=True,
            # provider_states_setup_url=f"{PROVIDER_URL}/_pact/provider_states",
            enable_pending=False,
        )
        assert success == 0
