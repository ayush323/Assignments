import pickle
file1 = open('/home/ayush/assignment3/multi.txt', "r")
listt = file1.readlines()
final = {}
for string in listt:
    tmp = string.split(',')
    tmp2 = []
    if tmp[0][2] != ':':
      val = int(tmp[0][2])
    else:
        break
    final[val] = [] 
    tmp1 = tmp[1:len(tmp)]
    for i in tmp1:
        if i == '\n':
            continue
        i = int(i)
        tmp2.append(i)
    final[val] = tmp2
print(final)
output = open('dic.pkl', 'wb')
pickle.dump(final, output)
output.close()
        
          
        
        
