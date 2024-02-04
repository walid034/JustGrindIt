class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reachTime = []
        for i in range(0, len(dist)):
            reachTime.append(dist[i]/speed[i])
        
        reachTime.sort()
        elim = 0

        for i in range(len(reachTime)):
            if reachTime[i] <= i:
                break
            elim+=1

        return elim
