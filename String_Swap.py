def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = []

        if s1 == s2:
            return True
                      
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps.append(i)
        
        if len(swaps) != 2:
            return False 

        i, j = swaps
        return s1[i] == s2[j] and s2[i] == s1[j]
                  
        