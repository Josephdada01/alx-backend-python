#!/usr/bin/env python3
"""A module that tests GithubOrgClient"""

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json",)
    def test_org(self, org: str, resp: Dict, mock_func: MagicMock) -> None:
        """Testing the org method."""
        # Set up the mock function to return the expected response
        mock_func.return_value = MagicMock(return_value=resp)

        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient(org)

        # Call the org method and assert the result
        self.assertEqual(github_org_client.org(), resp)

        # Assert that get_json was called with the correct URL
        mock_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )


if __name__ == '__main__':
    unittest.main()
