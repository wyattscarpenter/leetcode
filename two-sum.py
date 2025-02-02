class Solution1:
    """This is the naive solution."""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if i != i2 and num+num2 == target:
                    return [i, i2]

class Solution2:
    """This is the, uh, 'expected' solution."""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {} # the number to the index
        for i, num in enumerate(nums):
            remainder = target-num
            if remainder in seen and (i2 := seen[remainder]) != i:
                return sorted([i, i2])
            seen |= {num: i}

# You could also do a big array (10**9*2 size array) method if you don't believe in hashmaps. It's perhaps more honorable that way.
# You could also use a set and it wouldn't be that bad. But you might as well use a hashmap then, like we did here.

Solution = Solution2
