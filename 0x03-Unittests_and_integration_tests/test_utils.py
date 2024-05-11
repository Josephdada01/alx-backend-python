#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


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
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple,
                               expected: Union[Dict, int]) -> None:
        """a method that test and return the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
