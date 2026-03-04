
n = int(input())
arr = list(map(int, input().split()))
 
anyOdd = any(i%2 != 0 for i in arr)
anyEven = any(i%2 == 0 for i in arr)
 
if anyOdd and anyEven:
    arr.sort()
 
print(*arr)