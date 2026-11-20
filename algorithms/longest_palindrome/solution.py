"""最长回文子串（LeetCode 5）

中心扩展法：枚举每个可能的回文中心，向两侧扩展。
时间复杂度 O(n²)，空间复杂度 O(1)。
"""

from __future__ import annotations


def longest_palindrome(s: str) -> str:
    """返回字符串 s 中的最长回文子串；若有多个，返回最先出现的那个。"""
    if not s:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        # 奇数长度：以 s[i] 为中心
        left1, right1 = _expand(s, i, i)
        # 偶数长度：以 s[i], s[i+1] 的间隙为中心
        left2, right2 = _expand(s, i, i + 1)

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start : end + 1]


def _expand(s: str, left: int, right: int) -> tuple[int, int]:
    """从 [left, right] 向两侧扩展，返回最长回文的左右闭区间下标。"""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


if __name__ == "__main__":
    examples = ["babad", "cbbd", "a", "ac", "aaaa"]
    for text in examples:
        print(f"{text!r} -> {longest_palindrome(text)!r}")
