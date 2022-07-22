N = open('24-2.txt')
s = N.readline()

k1 = 0
k2 = 0
while len(s) > 0:

    # 1 решение
    if s.count('C') > s.count('D'):
        k1 += 1

    # 2 решение
    c = 0
    d = 0
    for i in s:
        if i == 'C':
            c += 1
        if i == 'D':
            d += 1

    if c > d:
        k2 += 1
    # конец второго решения

    s = N.readline()

print(k1)
print(k2)
