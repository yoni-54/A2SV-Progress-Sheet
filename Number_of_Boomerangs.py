class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for x1, y1 in points:
            defdict = defaultdict(int)
            for x2, y2 in points:
                dx = x2 - x1
                dy = y2 - y1
                d = dx*dx + dy*dy
                defdict[d] +=1
            for k in defdict.values():
                total += k * (k-1)
        return total