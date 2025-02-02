def stuple(*args):
    """sorted tuple constructor"""
    return tuple(sorted(args))

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """the naive, but pretty, solution (it timelimits on 260 / 313 testcases passed)"""
        return [
            list(s) for s in {
                stuple(num1, num2, num3)
                for i, num1 in enumerate(nums)
                for j, num2 in enumerate(nums)
                for k, num3 in enumerate(nums)
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0
            }
        ]

from collections import defaultdict

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Let us skip over the obvious solution that is n³ and instead consider how my two sum might be extended to the three sum. Hard to immediately see how to get better than O(n²)...
        Actually the problem is quite different in favor, really
        timelimit exceeded on 308 / 313 testcases passed"""
        target = 0
        results = set()
        pairs: dict[int, set[tuple(int, int)]] = defaultdict(set) # the number to the indexes
        for i, n in enumerate(nums):
           for j, n2 in enumerate(nums):
               if i != j:
                   pairs[n+n2].add(stuple(i,j))
        for k, num in enumerate(nums): 
            if -num in pairs:
                for candidate_pair in pairs[-num]:
                    print(candidate_pair)
                    i, j = candidate_pair
                    if k not in {i, j}:
                        results.add(stuple(nums[k], nums[i], nums[j]))
        return [list(s) for s in results]


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Isomorphically to 2sum, we could also do it this n² way.
        Time Limit Exceeded on (309 / 313 testcases passed)"""
        results = set()
        seen: dict[int, set[int]] = defaultdict(set) # the number to the set of indexes that support it
        target = 0
        for i, n in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j:
                    remainder = target-n-n2
                    if remainder in seen:
                        for candidate_index in seen[remainder]:
                            if candidate_index not in {i, j}:
                                results.add(stuple(remainder, n, n2))
            seen[n].add(i)
        return [list(t) for t in results]

class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """The previous solution with just a couple more marginal performance improvements. 312 / 313 testcases passed"""
        results = set()
        seen: dict[int, set[int]] = defaultdict(set) # the number to the set of indexes that support it
        target = 0
        for i, n in enumerate(nums):
            for j, n2 in enumerate(nums[:i]):
                if i > j:
                    remainder = target-n-n2
                    if remainder in seen:
                        for candidate_index in seen[remainder]:
                            if candidate_index not in {i, j}:
                                results.add(stuple(remainder, n, n2))
                                break
            if n not in seen:
                seen[n].add(i)
        return [list(t) for t in results]

class Solution5:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Solution 2 with some improvements. Still times out at 308 / 313 testcases passed."""
        target = 0
        results = set()
        pairs: dict[int, set[tuple(int, int)]] = defaultdict(set) # the number to the component parts
        for i, n in enumerate(nums):
            if -n in pairs:
                for p0, p1 in pairs[-n]:
                    results.add(stuple(n, p0, p1))
            for j, n2 in enumerate(nums[:i]):
                pairs[n+n2].add(stuple(n,n2))
        return [list(s) for s in results]

class Solution6:
    """Time out on 308 / 313 testcases passed"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        results = set()
        singles = set()
        pairs: dict[int, set[tuple(int, int)]] = defaultdict(set) # the number to the component parts
        for n in nums:
            if -n in pairs:
                for p0, p1 in pairs[-n]:
                    results.add(stuple(n, p0, p1))
            for n2 in singles:
                pairs[n+n2].add(stuple(n,n2))
            singles.add(n)
        return [list(s) for s in results]

from functools import cache

class Solution7:
    """*Literally* just use two sum. Plus a couple of enhancements. Still times out on 309 / 313 testcases passed though."""
    @cache
    def twoSum(self, nums: tuple[int], target: int, exclude: int|None = None) -> set[tuple[int, int]]:
        seen: dict[int, int] = {} # the number to the index
        res = set()
        for i, num in enumerate(nums):
            if i == exclude:
                continue
            remainder = target-num
            if remainder in seen and (i2 := seen[remainder]) != i:
                res.add(stuple(i, i2))
            seen |= {num: i}
        return res
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = set()
        for i, num in enumerate(nums):
            for res in self.twoSum(tuple(nums[:i]), -num, exclude=i):
                index1, index2 = res
                if i not in res:
                    results.add(stuple(num, nums[index1], nums[index2]))
        return [list(s) for s in results]

class Solution8:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Solution4 but with another special case"""
        if not any(nums):
            return [[0,0,0]]
        else:
            return Solution4().threeSum(nums)

Solution = Solution8