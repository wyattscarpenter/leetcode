"""(unfinished)"""

class Solution1:
    """Linear search"""
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for interval in intervals:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                pass
            elif interval[0] < newInterval[0] and interval[1] >= newInterval[0]:
                intervals.remove(interval)
                return self.insert(intervals, [interval[0], newInterval[1]])
            elif interval[0] >= newInterval[0]:
                ... #got bored

class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        b, e = newInterval
        return [[i,j] for i, j in invervals if i < b and j < b]
        + [min([i for i, j in intervals + [newInterval] if i>= j > newInterval[1] and interval[1] < newInterval[0] ] )]
        ... #also got bored


