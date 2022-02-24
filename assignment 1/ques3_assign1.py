i = 0
p = 1
n = int(input("enter number of lines"))
while i <= n:
    if i < n // 2:
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
    
    
