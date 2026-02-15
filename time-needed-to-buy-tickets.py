class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        "Uh, let's just... simulate it, I suppose"
        t = 0 
        while True:
            t+=1
            k-=1
            jimmy = tickets.pop(0)
            jimmy -= 1
            if jimmy == 0:
                if k == -1:
                    return t
            else:
                tickets.append(jimmy)
            if k == -1:
                k = len(tickets)-1
