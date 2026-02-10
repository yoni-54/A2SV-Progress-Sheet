def soldierAndBananas(k, n, w):
    sum = 0
    for i in range(1, w+1):
        sum += i*k
    borrow = sum - n
    return max(0, borrow)
 
k, n, w=map(int, input().split())
 
print(soldierAndBananas(k, n, w))