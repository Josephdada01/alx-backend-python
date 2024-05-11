#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from . import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits
    from unittest.TestCase.Implement the TestAccessNestedMap.
    test_access_nested_map method to test that the method
    returns what it is supposed to.
    Decorate the method with @parameterized.expand to test
    the function for following inputs:
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expec_res):
        self.assertEqual(utils.access_nested_map(nested_map, path), expec_res)


if __name__ == '__main__':
    unittest.main()
