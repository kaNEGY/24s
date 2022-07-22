N = open('24-1.txt')
s = N.readline()


book = ['LOL']
max_len = 0
for i in s:
    if ((book[-1] == 'R' and i == 'A') or (book[-1] == 'A' and i == 'S') or
            (book[-1] == 'S' and i == 'I') or (book[-1] == 'I' and i == 'Y')
            or (book[-1] == 'Y' and i == 'A') or book[-1] == i):
        book.append(i)
    else:
        if ('R' in book and 'A' in book and 'S' in book and 'I' in book
                and 'Y' in book and book[-1] == 'A'):
            max_len = max(max_len, len(book))
        book = [i]
print(max_len)
