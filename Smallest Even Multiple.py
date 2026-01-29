def smallestEvenMultiple(n):
    if n % 2 == 0:
        return n    
    else:
        return n * 2

t = int(input())
smallestEvenMultiple(t)