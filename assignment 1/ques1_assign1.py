s1 = input("enter the first string")
s2 = input("enter the second string")
flag = 0
for i in s2:
    if i not in s1:
        flag = 1
        print("set of tiles can not spell the word")
        break
if flag == 0:
    print("set of tiles can spell the world")
    
