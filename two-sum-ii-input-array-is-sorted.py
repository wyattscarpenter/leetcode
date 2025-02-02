class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Time Limit Exceeded 0/24"""
        left_index = len(numbers)//2
        right_index = left_index+1
        original_right_index = right_index
        while left_index+right_index != target:
            if right_index == len(numbers)-1:
                left_index -= 1
                right_index = original_right_index
        return [left_index+1, right_index+1]

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """timeout 20 / 24 testcases passed"""
        for i, n in enumerate(numbers):
            for j, n2 in enumerate(numbers[i+1:], start=i+1):
                if n+n2 == target:
                    return [i+1, j+1]
                elif n+n2 > target:
                    break
class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ok, fine, I will write binary search, alright? (it worked)"""
        for i, n in enumerate(numbers):
            #binary search
            leftmost = i+1
            rightmost = len(numbers)-1
            while True:
                index = (leftmost+rightmost)//2
                print(leftmost, index, rightmost)
                n2 = numbers[index]
                sum = n+n2
                if sum == target:
                    return [i+1, index+1]
                elif leftmost == rightmost:
                    #if the bounds are the same, then the search is exhausted
                    break
                elif sum > target:
                    rightmost = index
                elif sum < target:
                    leftmost = index+1

class Solution4:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """I was circling this in my mind but didn't have the concept exactly right until I read some solutions (specifically https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/51253/a-simple-o-n-solution/ )"""
        n = numbers
        l = 0
        r = len(n) - 1
        while (sum := n[l] + n[r]) != target:
            if sum > target:
                r-=1
            else:
                l+=1
        return [l+1, r+1]

Solution = Solution4