from collections import Counter
# BTW, the best algorithm here relies on the precise nature of a majority (not just a plurality) and is the Boyer–Moore majority vote algorithm, which has an excellent wikipedia illustration here: https://upload.wikimedia.org/wikipedia/commons/c/c7/Boyer-Moore_MJRTY.svg
# I did not implement that.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
