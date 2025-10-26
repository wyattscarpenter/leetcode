class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = lambda x: ''.join(sorted(x)) #garbage language needs workaround
        peter = defaultdict(list)
        for s in strs:
            # OK, so, technically we do not need to sort, only hash in an order-independent way, such as sum up all the letters (to use a bad, toy example); this would also improve our time complexity. However, I do not care.
            peter[sorts(s)].append(s)
        return list(peter.values())
