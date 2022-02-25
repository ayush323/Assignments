listt = []
order = int(input("enter how many order you want to add = "))
k = 1
for i in range(order):
    tmpl = []
    tmpl.append(k)
    n = int(input("how many books you want to add in yur order = "))
    books = []
    for j in range(n):
        s = input("enter book no")
        books.append(s)
        q = int(input("enter quantity = "))
        books.append(q)
        price = float(input("enter the price per unit = "))
        books.append(price)
        fin = tuple(books)
        tmpl.append(fin)
        books = []
    listt.append(tmpl)
    k += 1
        
    
final = []
for tmp_list in listt:
    tmp = []
    ammount = 0
    for i in range(len(tmp_list)):
        if i == 0:
            tmp.append(tmp_list[i])
        else:
            value = tmp_list[i][1]*tmp_list[i][2]
            ammount += value
    tmp.append(ammount)
    new = tuple(tmp)
    final.append(new)
    
print(final)         
