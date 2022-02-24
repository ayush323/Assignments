from collections import Counter
votes = input("enter the names of the candidates name should be space separated").split()

freq = Counter(votes)
count = []
for i in freq.values():
    count.append(i)
maxx = max(count)
final = []
for i in freq:
    if freq[i] == maxx:
        final.append(i)
final.sort()
print(final[0])
