from collections import Counter as C
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """modify 'in-place' as instructed."""
        c = C(nums)
        nums.clear()
        for color, count in sorted(c.items()):
            nums.extend([color]*count)
