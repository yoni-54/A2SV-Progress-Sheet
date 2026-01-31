class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict = {}
        for winner, loser in matches:
            if winner not in dict:
                dict[winner] = 0
            if loser not in dict:
                dict[loser] = 1
            else:
                dict[loser] += 1
        not_lost=[]
        lost_once=[]
        for num in sorted(dict.keys()):
            if dict[num] == 0:
                not_lost.append(num)
            elif dict[num] == 1:
                lost_once.append(num)
        return [not_lost, lost_once]
