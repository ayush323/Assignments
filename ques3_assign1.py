i = 0
p = 1
while i <= 10:
    if i < 5:
        k = 0
        while k < p:
            print('*', end = ' ')
            k += 1    
        p += 1    
    else:
        k = 0
        while k < p:
            print('*', end = ' ')
            k += 1
        p -= 1    
    i += 1
    print()
    
    
