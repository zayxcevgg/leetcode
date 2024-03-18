class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    haystack = "sadbutsad"
    needle = "sad"
    strStr(0, haystack, needle)