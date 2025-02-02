"""The prompt for this one includes "You must write an algorithm that runs in O(n) time and without using the division operation.", which forecloses certain possibilities.

We are DONE saying "followup: can you give the good solution tho?"; good solutions FIRST 😤"""

from functools import cache

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """This is (or can be) a classic memoiztion-type problem, which is to say I'm going to use functools.cache, ie a hashmap.
        However, this exceeded the memory limit, :/"""
        last_num_index = len(nums) - 1
        @cache
        def product_of(start, end):
            """Both sides of this are inclusive btw"""
            if end < 0 or start > last_num_index:
                return 1 # multiplicative identity
            if start == end:
                return nums[end]
            else:
                return product_of(start, end-1) * product_of(end, end)

        return [product_of(0, i-1) * product_of(i+1, last_num_index) for i, _ in enumerate(nums)]
