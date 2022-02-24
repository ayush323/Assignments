
s = "12345"*5
i = 0
while i < len(s):
    print(s[i],end = '')
    i += 5
i = 4
print()
while i < len(s):
    print(s[i], end = '')
    i += 5
listt = []
print()
for i in s:
    listt.append(i)
listt.reverse()
tmp = ''
s = tmp.join(listt)
print(s)
