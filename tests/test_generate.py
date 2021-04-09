import pytest
from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    assert generate_diff("tests/fixtures/file1.json",
                         "tests/fixtures/file2.json") == " - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n"
                         