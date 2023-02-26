#!/usr/bin/env python3
"""Python module to test the utils program"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the utils.access_nested_map
    from utils.py"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """Testing the access_nested_map output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ) -> None:
        """Testing the access_nested_map exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
