t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    possible_A = False
    possible_B = False
    
    for X in range(1, n+1):
        a_sets = 0
        b_sets = 0
        a_points = 0
        b_points = 0
        last_winner = None
        
        for ch in s:
            if ch == 'A':
                a_points += 1
            else:
                b_points += 1
            
            if a_points == X:
                a_sets += 1
                a_points = 0
                b_points = 0
                last_winner = 'A'
            elif b_points == X:
                b_sets += 1
                a_points = 0
                b_points = 0
                last_winner = 'B'
        
        if a_points != 0 or b_points != 0:
            continue
        
        if a_sets > b_sets and last_winner == 'A':
            possible_A = True
        if b_sets > a_sets and last_winner == 'B':
            possible_B = True
    
    if possible_A and not possible_B:
        print("A")
    elif possible_B and not possible_A:
        print("B")
    else:
        print("?")