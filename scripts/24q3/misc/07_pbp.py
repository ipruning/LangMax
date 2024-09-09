import pdb

pdb.set_trace()


def g(data):
    return data * data


def f(x):
    breakpoint()
    lst = []
    for i in range(x):
        val = g(i)
        lst.append(val)
    return lst


f(3)

# Example of pdb commands

# p x
# w
# l
# ll

# 上一个帧
# u
# p x
# 当前帧
# d
# p x

# n 运行
# p list
