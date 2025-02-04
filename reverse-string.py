class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #presumably s is an array bc strings are immutable in python
        print("".join(s))
        i=0
        while i < len(s)//2:
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
            i+=1
        print("".join(s))

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

Solution = Solution1
