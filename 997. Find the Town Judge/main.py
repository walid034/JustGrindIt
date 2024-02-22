class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0]*(n+1)
        trusted = [0]*(n+1)

        for pair in trust:
            trusted[pair[1]] += 1
            trusts[pair[0]] += 1

        mayor = -1

        for i in range(1, n+1):
            if trusts[i] == 0 and trusted[i] == n-1:
                mayor = i
        
        return mayor
