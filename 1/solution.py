e, c = [], 0
for l in open('input.txt'):
    if l != '\n':
        c += int(l)
    else:
        e.append(c)
        c = 0

e.sort(reverse = True)

print(e[0])
print(sum(e[0:3]))

