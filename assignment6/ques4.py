def cal_sum(listt):
    print(sum(listt))


def calc_evennumSum(func):
    def inner(listt):
        tmp = []
        for i in listt:
            if i % 2 == 0:
                tmp.append(i)
        return func(tmp)
    return inner
def calc_sum(func):
    def inner(listt):
        return func(listt)
    return inner
@calc_sum
def even_sum(listt):
     s = sum(listt)
     if s % 2 != 0:
         s = s + 1
         return s
     else:
         return s

cal_sum = calc_evennumSum(cal_sum)
new = list(map(int, input("enter the space separated list").split()))
cal_sum(new)
print(even_sum(new))
