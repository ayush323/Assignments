def pallindrome(num):
    tmp = str(num)
    listt = []
    for i in tmp:
        listt.append(i)
    listt2 = list(reversed(listt))
    for i in range(len(listt)):
        if listt[i] != listt2[i]:
            return 0
    return 1

start = 10
while start < 999999:
    if pallindrome(start):
        print(start)
    start += 1    
