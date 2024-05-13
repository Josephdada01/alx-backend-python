#!/usr/bin/env python3
"""A module that tests GithubOrgClient"""

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """a method that test public repo make it return a known payload."""
        # Patch the org method to return the mock payload
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock,) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos", }
            # Create an instance of GithubOrgClient
            self.assertEqual(GithubOrgClient("google")
                             ._public_repos_url,
                             "https://api.github.com/users/google/repos",)


if __name__ == '__main__':
    unittest.main()
