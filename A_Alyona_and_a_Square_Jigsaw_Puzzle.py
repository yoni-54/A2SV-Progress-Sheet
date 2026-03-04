import math

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    happy = 0
    
    for x in arr:
        total += x
        
        root = int(math.isqrt(total))
        
        if root * root == total and root % 2 == 1:
            happy += 1
    
    print(happy)