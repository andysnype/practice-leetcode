from functools import reduce


def productList(numbers):
    ans = []
    for i in range(len(numbers)):
        lhs = reduce(lambda total, val: total * val, numbers[:i], 1)
        rhs = reduce(lambda total, val: total * val, numbers[i+1:], 1)
        ans.append(lhs * rhs)
    return ans
