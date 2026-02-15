class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """IDK man there's probably some closed-form solution for this like n-k or k%n or something
        but since I don't know that, I'm going to go it... the long way!
        Update: even though this is listed as a medium, this simple solution still 'Beats 100%' (everyone got it)"""
        friends = list(range(1,n+1)) # note that this doesn't match the 0-indexing we use for the rest of the prob
        index = 0
        while len(friends) > 1:
            index = (index + (k-1)) % len(friends)
            friends.pop(index)
        return friends[0]
