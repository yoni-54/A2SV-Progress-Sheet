import sys
n = int(input())

phoneBook={}
for _ in range(n):
    entry = input().split()
    name = entry[0]
    phoneNumber = entry[1]
    phoneBook[name] = phoneNumber
    
for query in sys.stdin:
    name = query.strip()
    
    if not name:
        break
    if name in phoneBook:
        print(f"{name}={phoneBook[name]}")
    else:
        print("Not found")