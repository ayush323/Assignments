from collections import Counter
votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]

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
