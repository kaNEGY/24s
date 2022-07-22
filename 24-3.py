N = open('24-3.txt')
s = N.readline()

summa = 0
third = 0
for i in range(len(s)):
    if s[i] == 'F':

        if third < 3:
            third += 1

            if third == 3:
                third = i + 1

        summa += (i + 1)

otvet = summa * third
print(otvet)
