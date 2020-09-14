"""
求阶乘和
1!+2!+3!+......+n!
"""


def func(num):
    result = 0
    tmp = 1
    for i in range(1, num + 1):
        tmp *= i
        result += tmp

    return result


if __name__ == '__main__':
    print(func(10))
