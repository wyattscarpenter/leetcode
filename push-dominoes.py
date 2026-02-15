class Solution:
    """the description of this problem is curiously written, but the problem itself is sound and interesting.
    The braindead™ way to solve it is to simulate all the steps. However, we can just compute a sort of closed-form solution
    by noting that the domino forces continue unless counteracted, in which case the resolution is in the middle.
    This allows us to solve it in linear time."""
    def pushDominoes(self, dominoes: str) -> str:
        # type domino_state = Literal[".", "L", "R"] #It's kind of a hassle to actually use this, but keep it in mind.
        # I attempted to solve this in a way that would be easy to follow, not minding verbosity; I don't think that gamble paid off.
        ret: str = ""
        u: str = "" # u for unresolved_domino_substring
        for d in dominoes:
            l = len(u) # l for length (of u)
            if d == "L":
                if u == "":
                    ret+="L"
                elif u[0] == ".":
                    ret += "L"*(l+1)
                    u = ""
                elif u[0] == "R":
                    #technically you could probably make this accomodate the empty case,
                    # but it's easier to follow this way
                    ret += "R"*((l+1)//2) + "."*((l+1)%2) + "L"*((l+1)//2)
                    u = ""
            elif d==".":
                u+=d
            elif d=="R":
                if u == "":
                    u+=d
                elif u[0] == "R":
                    ret+="R"*l
                    u = "R"
                else:
                    ret+=u
                    u = "R"
        #clean up anything unresolved now that we're off the right edge
        if u != "":
            l = len(u)
            if u[0] == "R":
                ret+="R"*l
            else:
                ret+="."*l
        return ret
