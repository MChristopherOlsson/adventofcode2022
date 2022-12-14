letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
p1, p2, count = 0, 0, 0
lines = []

for line in open("input.txt"):
    l = line.rstrip()
    lines.append(l)
    count += 1
    
    # Solution 1
    m = len(l) // 2
    firstHalf, secondHalf = set(l[:m]), set(l[m:])
    c = firstHalf.intersection(secondHalf).pop()
    p1 += letters.find(c) + 1

    # Solution 2
    if count % 3 == 0:
        x = set(lines[count - 3])
        y = set(lines[count - 2])
        z = set(lines[count - 1])
        c = x.intersection(y,z).pop()
        p2 += letters.find(c) + 1

print(f"Solution 1: {p1}")
print(f"Solution 2: {p2}")

