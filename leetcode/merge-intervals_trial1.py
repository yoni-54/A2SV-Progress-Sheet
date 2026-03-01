class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = [intervals[0]]

        for current in intervals:
            last = merge[-1]
            if current[0] <= last[1]:
                last[1] = max(current[1], last[1])
            else:
                merge.append(current)
        return merge
