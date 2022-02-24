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

cal_sum = calc_evennumSum(cal_sum)
new = list(map(int, input("enter the space separated list").split()))
cal_sum(new)
