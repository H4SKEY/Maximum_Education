# Экзамен MAXIMUM осень 2025
# 2
print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x or not(y)) and not(y == z) and w: print(x, y, z, w)

print('zwyx')

# 5
def convert(n, sys):
    s = ''

    while n != 0:
        s += str(n % sys)
        n //= sys

    return s[::-1]


for i in range(2, 1000):
    n = convert(i, 3)

    if i % 3 == 0: n = f'{n}{n[-2:]}'
    else: n = f'{n}{convert((i % 3) * 5, 3)}'

    r = int(n, 3)

    if r >= 86:
        print(i)
        break

# 6
print((25 * 2) + (25 * 2))
# from turtle import *

# tracer(0)
# screensize(4000, 4000)
# left(90)
# m = 40

# for i in range(9):
#     forward(27 * m)
#     right(90)
#     forward(30 * m)
#     right(90)

# up()
# forward(3 * m)
# right(90)
# forward(6 * m)
# left(90)
# down()

# for i in range(9):
#     forward(77 * m)
#     right(90)
#     forward(66 * m)
#     right(90)

# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(5, 'red')

# done()

# 8
from itertools import product as p

words = [''.join(i) for i in p('косуф', repeat=5)]
result = list(filter(lambda x: x.count('ф') == 0 and x.count('у') == 2, words))
print(words.index(result[-1]) + 1)

# 9
from os import path
from collections import Counter


def count_3(array):
    return len(set(array)) == 4


def square(array):
    triple = [i for i, j in Counter(array).items() if j == 3]

    if len(triple) > 0:
        triple = triple[0]
        return pow(triple, 2) * 3 > sum(pow(i, 2) for i, j in Counter(array).items() if j == 1)

file_path = path.join(path.dirname(path.abspath(__file__)), '9_1.txt')
nums = [sorted(int(j) for j in i.split()) for i in open(file_path, encoding='utf-8')]
print(len([i for i in nums if count_3(i) and square(i)]))

# 13
from ipaddress import ip_network
print(ip_network('98.81.154.195/255.252.0.0', 0)[-2])


# 14
from string import digits, ascii_uppercase


def convert_to_25(num):
    alphabet, result, neg, abs_num = digits + ascii_uppercase[:15], '', num < 0, abs(num)

    if num == 0: return '0'

    while num > 0:
        num, rem = divmod(num, 25)
        result = alphabet[rem] + result

    return result


num = pow(169, 2023) - 7 * pow(24, 2024) + pow(984, 2025) - 6561
print(len([i for i in convert_to_25(num) if i in ascii_uppercase[6:]]))

# 15
p, q, a = list(range(117, 159)), list(range(129, 181)), []

for x in range(-1000, 1000):
    if not((x in p) <= (((x in q) and not(x in a)) <= (not(x in p)))): a.append(x)

print(max(a) - min(a))

# 16
def f(n):
    if n == 1: return 1
    if n > 1: return 2 * g(n - 1) + 3


def g(n):
    if n == 1: return 2
    if n > 1: return f(n - 1) + n


print(f(20) * g(26))


# 17
file_path = path.join(path.dirname(path.abspath(__file__)), '17_1 (1).txt')
nums = list(map(int, open(file_path, encoding='utf-8')))
min_pos = min(list(filter(lambda x: x > 0 and x % 110 == 0, nums)))
result = [i + j for i, j in zip(nums, nums[1:]) if (i + j) < min_pos]
print(len(result), abs(max(result)))


# 19 20 21
def play(s1, s2, k):
    if k < 0: return 0
    if s1 + s2 >= 107: return k % 2 == 0

    h = [play(s1 + 1, s2, k - 1), play(s1, s2 + 1, k - 1), 
         play(s1 * 2, s2, k - 1), play(s1, s2 * 2, k - 1)]
    
    return all(h) if k % 2 == 0 else any(h)


print(24) # print(min([i for i in range(1, 94) if play(13, i, 2)])) return any(h)
print(*[i for i in range(1, 94) if play(13, i, 3) > play(13, i, 1)])
print(min([i for i in range(1, 94) if play(13, i, 4) > play(13, i, 2)]))


# 23
def foo(x, y):
    if x > y or x == 15: return 0
    if x == y: return 1
    else: return foo(x + 1, y) + foo(x * 2, y) + foo(x * 3, y)


print(foo(1, 11) * foo(11, 25))


# 24
print(628)
# file_path = path.join(path.dirname(path.abspath(__file__)), '24_1.txt')
# s, count, mx, l = open(file_path, encoding='utf-8').readline(), 0, 0, 0

# for i in range(1, len(s)):
#     if s[i - 1] + s[i] == 'AB':
#         count += 1

#     while count > 110:
#         if s[l] + s[l + 1] == 'AB':
#             count -= 1
        
#         l += 1
    
#     if count == 110: mx = max(mx, i - l + 1)

# print(mx)

# 25
from fnmatch import fnmatch

for i in range(2023, pow(10, 8), 2023):
    if fnmatch(str(i), '1*23?9'): print(i, i // 2023)

# 26
file_path = path.join(path.dirname(path.abspath(__file__)), '26_1.txt')
n = list(map(int, open(file_path, encoding='utf-8').readlines()))[0]
boxes = sorted(list(map(int, open(file_path, encoding='utf-8').readlines()))[1:])[::-1]
data, count = boxes[0], 1

for i in range(1, len(boxes)):
    if data - boxes[i] >= 10:
        count += 1
        data = boxes[i]

print(count, data)

# 27
from math import dist

file_path_a = path.join(path.dirname(path.abspath(__file__)), '27_А.txt')
file_path_b = path.join(path.dirname(path.abspath(__file__)), '27_Б.txt')
cluster_a = [[], []]

for i in open(file_path_a, encoding='utf-8'):
    x, y = [float(j.replace(',', '.')) for j in i.split()]

    if y > 15: cluster_a[0].append([x, y])
    elif y < 15: cluster_a[1].append([x, y])

cluster_b = [[], [], []]

for i in open(file_path_b, encoding='utf-8'):
    x, y = [float(j.replace(',', '.')) for j in i.split()]
    
    if y > 4 and x > 2: cluster_b[0].append([x, y])
    elif y < 4 and x > 2: cluster_b[1].append([x, y])
    elif y < 4 and x < 2: cluster_b[2].append([x, y])


def find_center(cluster):
    result = []

    for i in cluster:
        s = sum(dist(i, j) for j in cluster)
        result.append([s, i])

    return min(result)[1]


center_a = [find_center(i) for i in cluster_a]
center_b = [find_center(i) for i in cluster_b]

px_a, py_a = sum([i for i, j in center_a]) / len([i for i, j in center_a]), sum([j for i, j in center_a]) / len([j for i, j in center_a])
px_b, py_b = sum([i for i, j in center_b]) / len([i for i, j in center_b]), sum([j for i, j in center_b]) / len([j for i, j in center_b])

print(int(px_a * 10_000), int(py_a * 10_000))
print(int(px_b * 10_000), int(py_b * 10_000))


