from functools import reduce


def productList(numbers):
    ans = []
    for i in range(len(numbers)):
        lhs = reduce(lambda total, val: total * val, numbers[:i], 1)
        rhs = reduce(lambda total, val: total * val, numbers[i+1:], 1)
        ans.append(lhs * rhs)
    return ans

    """[This is a cached approach that has 3 iterations per number]
    """


def productList2(numbers):
    ans = []
    lhs = [1]
    rhs = [1]
    lhsProd = 1
    rhsProd = 1
    for val in numbers[:-1]:
        lhsProd *= val
        lhs.append(lhsProd)
    for val in numbers[:0:-1]:
        rhsProd *= val
        rhs.insert(0, rhsProd)
    for i in range(len(numbers)):
        ans.append(lhs[i] * rhs[i])
    return ans


if __name__ == '__main__':
    print(productList2([2, 3, 5, 4]))
