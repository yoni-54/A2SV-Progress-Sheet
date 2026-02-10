
def wayToLong(arr):
    result = []
    for a in arr:
        newWord = ""
        if len(a) > 10:
            newWord = a[0] + str(len(a)-2) + a[-1]
            result.append(newWord)
        else:
            result.append(a)
    return result
    
n = int(input())
arr = [input() for _ in range(n)]
print('\n'.join(wayToLong(arr)))