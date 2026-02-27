n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

if k == 0:
    if arr[0] == 1:
        print(-1)
    else:
        print(arr[0] - 1)

else:
    x = arr[k - 1]
    
    if k == n:
        print(x)
    elif arr[k] == x:
        print(-1)
    else:
        print(x)