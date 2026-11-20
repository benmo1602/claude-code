"""最长回文子串单元测试。"""

import unittest

from solution import longest_palindrome


class TestLongestPalindrome(unittest.TestCase):
    def test_odd_length(self) -> None:
        result = longest_palindrome("babad")
        self.assertIn(result, {"bab", "aba"})

    def test_even_length(self) -> None:
        self.assertEqual(longest_palindrome("cbbd"), "bb")

    def test_single_char(self) -> None:
        self.assertEqual(longest_palindrome("a"), "a")

    def test_two_different_chars(self) -> None:
        result = longest_palindrome("ac")
        self.assertIn(result, {"a", "c"})

    def test_all_same(self) -> None:
        self.assertEqual(longest_palindrome("aaaa"), "aaaa")

    def test_empty(self) -> None:
        self.assertEqual(longest_palindrome(""), "")

    def test_full_string_palindrome(self) -> None:
        self.assertEqual(longest_palindrome("racecar"), "racecar")

    def test_returns_first_when_tied(self) -> None:
        # "aa" 出现在索引 0 和 1；应返回最先出现的 "aa"（索引 0..1）
        self.assertEqual(longest_palindrome("aaa"), "aaa")


if __name__ == "__main__":
    unittest.main()
