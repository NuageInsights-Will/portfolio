from func_string_rev import string_rev
import pytest

def test_string_rev() -> None:
    assert string_rev("hello") == "olleh"
    assert string_rev("Hello, world!") == "!dlrow ,olleH"
    assert string_rev("") == ""
    assert string_rev("123")  == "321"