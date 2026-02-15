def g(array, index):
    """safe get"""
    try:
        return array[index]
    except:
        return "0"  # this dummy value only works for this application


def cmp(p, word, order):
    """This is really just factored out for flow-control reasons."""
    #print(p, word, order) #nb: embarassingingly, I forgot which side pop popped from until I logged this
    l = max(len(p), len(word))
    for i in range(l):
        #print(g(p, i), g(word, i))
        # find returns -1 if not found, which is nice for us because the non-existent character comes first
        ord_prev = order.find(g(p, i))
        ord_curr = order.find(g(word, i))
        if ord_prev > ord_curr:
            return False
        if ord_prev < ord_curr:
            return True
    return True #although not explicitly specified, they do actually expect equal words to be considered "sorted"


class Solution:
    """True to its word, this leetcode problem is easy. Since we can just do the pairwises."""

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        p = words.pop(0)  # previous word
        for word in words:
            r = cmp(p, word, order)
            if not r:
                return False
            p = word
        return True
