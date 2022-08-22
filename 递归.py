# def fuc(x):
#     if x > 0:
#         print(x)
#         fuc(x - 1)
#
#
# fuc(3)
#
#
# def a(x):
#     if x > 0:
#         a(x - 1)
#         print(x)
#
#
# a(3)

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('移动  %s 到 %s' % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, 'a', 'b', 'c ')
