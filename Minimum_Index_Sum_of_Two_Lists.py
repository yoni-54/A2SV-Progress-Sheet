class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        minSum = float("inf")

        for i in range(len(list1)):

            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s = i + j
                    if s < minSum:
                        minSum = s
                        result = [list1[i]]
                    elif s == minSum:
                        result.append(list1[i])
        return result