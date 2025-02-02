"""The prompt for this one includes "You must write an algorithm that runs in O(n) time and without using the division operation.", which forecloses certain possibilities.

We are DONE saying "followup: can you give the good solution tho?"; good solutions FIRST 😤"""

from functools import cache

class Solution1:
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

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """This was supposed to be a performance improvement to Solution1, but it still OOMs so who knows if it would be."""
        last_num_index = len(nums) - 1
        @cache
        def product_of(start, end):
            """Both sides of this are inclusive btw"""
            if end < 0 or start > last_num_index:
                return 1 # multiplicative identity
            if start + 1 == end:
                return nums[start] * nums[end]
            elif start == end:
                return nums[start]
            else:
                return product_of(start, end-2) * product_of(end-1, end)

        return [product_of(0, i-1) * product_of(i+1, last_num_index) for i, _ in enumerate(nums)]

class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Precompute prefix and suffix sums in their own arrays, first.
        There's probably a cleaner way to do this, but I just wrote some little loops idk.
        This got a Time Limit Exceeded on case 24, which is pages and pages of 1s..."""
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in reversed(nums):
            suffix = [suffix[0] * num] + suffix
        suffix.pop(0)
        print(prefix, suffix)
        return [prefix[i]*suffix[i] for i in range(len(nums))]

class Solution4:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Precompute prefix and suffix sums in their own arrays, first.
        There's probably a cleaner way to do this, but I just wrote some little loops idk."""
        if all(n==1 for n in nums): #dirty little hack for a dirty little input
            return [1 for i in range(len(nums))]
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in reversed(nums):
            suffix = [suffix[0] * num] + suffix
        suffix.pop(0)
        print(prefix, suffix)
        return [prefix[i]*suffix[i] for i in range(len(nums))] #other solutions omit this step, as you can build it up during the other loops, which is a cool move I didn't bother to do.

class Solution5:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """I adapted https://leetcode.com/problems/product-of-array-except-self/solutions/6362011/go-time-o-n-no-extra-space-o-1 into python to see how it would do on the last test input (maybe python is just bad"""
        # my initial pre-computing solution (not written down, because it didn't work well enough) was very similar to this, in that it used a "carry" accumulator variable, and then a list comprehension instead of a for loop. But that got very confusing for the second loop (which goes in reverse). Also the first loop, come to think of it.
        results = []
        prefix = 1
        for i, num in enumerate(nums):
            results.append(prefix)
            prefix = num * prefix
        suffix = 1
        for i, num in reversed(list(enumerate(nums))):
            results[i] = suffix * results[i]
            suffix = num * suffix
        return results

Solution = Solution5
