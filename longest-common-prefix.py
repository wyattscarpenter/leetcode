class Solution:
    def longestCommonPrefix1(self, strs: list[str]) -> str:
        """This works well, but times out on the arbitary time limit on leetcode."""
        s = ""
        while s != strs[0]:
            s += strs[0][len(s)]
            for ss in strs:
                if ss[:len(s)-1] != s:
                    s = s[:len(s)-1]
        return s
    
    def longestCommonPrefixEasy(self, strs: list[str]) -> str:
        from os.path import commonprefix
        return commonprefix(strs)
    def prefix(self, s1: str, s2: str) -> str:
        """Find the common prefix of two strings."""
        i = 0
        try:
            while True:
                if s1[i] == s2[i]:
                    i += 1
                else:
                    return s1[:i]
        except IndexError: #What a garbage programming language. No .get on str/list...
            return s1[:i]
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        """What if we needed to reimplment commonprefix, for example?"""
        s = strs.pop()
        for ss in strs:
            s = self.prefix(s, ss)
        return s
    def prefix_int(self, s1: str, s2: str, n: int|None = None) -> int:
        """Find the common prefix of two strings, up to n"""
        i = 0
        try:
            while True:
                if s1[i] == s2[i]:
                    if n is not None and i == n:
                        return i
                    i += 1
                else:
                    return i
        except IndexError: #What a garbage programming language. No .get on str/list...
            return i
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """OK well the previous one was cool but let's optimize performance a little."""
        prefix_i = None
        old_ss = strs.pop()
        for ss in strs:
            prefix_i = self.prefix_int(old_ss, ss, prefix_i)
            old_ss = ss
        return old_ss[:prefix_i]
