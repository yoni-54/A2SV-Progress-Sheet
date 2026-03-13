n, t = map(int, input().split())
 
arr = list(map(int, input().split()))
 
sum = 0
left = 0
max_book = 0
 
for r in range(len(arr)):
    sum += arr[r]
    
    while sum > t:
        sum -= arr[r]
        left += 1
        
    max_book = max(max_book, r-left+1)
    
print(max_book)
    
