n = int(input())
 
for _ in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    isPossible = True
    
    for i in range(1, t):
        if arr[i] - arr[i-1] > 1:
            isPossible = False
            break
            
    if isPossible:
        print("YES")
    
    else:
        print("NO")