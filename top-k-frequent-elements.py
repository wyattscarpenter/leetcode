from collections import Counter as C
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [x for x, _count in C(nums).most_common(k)]