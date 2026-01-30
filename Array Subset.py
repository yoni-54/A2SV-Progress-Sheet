from collections import Counter

class Solution:
    def isSubset(self, a, b):
        inventory = Counter(a)
        
        for num in b:
            if inventory[num] > 0:
                inventory[num] -= 1
            else:
                return False
                
        return True