def stuple(*args):
    """sorted tuple constructor"""
    return tuple(sorted(args))

def threeSum(nums: List[int], target: int, exclude: int|None = None) -> set[tuple[int]]:
    results = set()
    seen: dict[int, set[int]] = defaultdict(set) # the number to the set of indexes that support it
    for i, n in enumerate(nums):
        if i == exclude:
            continue
        for j, n2 in enumerate(nums[:i]):
            if j == exclude:
                continue
            if i > j:
                remainder = target-n-n2
                if remainder in seen:
                    for candidate_index in seen[remainder]:
                        if candidate_index not in {i, j}:
                            results.add(stuple(remainder, n, n2))
                            break
        if n not in seen:
            seen[n].add(i)
    return results

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Is this just 3sum, but again?"""
        #if not any(nums):
        #    return [[0,0,0,0]]
        results = set()
        for i, num in enumerate(nums):
            for result in threeSum(nums, target-num, exclude=i):
                results.add(stuple(num, *result))
        return [list(t) for t in results]

#PS: https://leetcode.com/problems/4sum/solutions/8545/python-140ms-beats-100-and-works-for-n-sum-n-2/ is kind of cool. It seems like for n>2 sum everyone's just using sorted 2-pointer and recursing down to 2sum (uninterestingly). So there you go.