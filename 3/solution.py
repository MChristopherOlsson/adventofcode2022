letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = 0

for data in open("input.txt"):
    lines = data.splitlines()
    for l in lines:
        m = len(l) // 2
        firstHalf, secondHalf = set(l[:m]), set(l[m:])
        c = firstHalf.intersection(secondHalf).pop()
        points += letters.find(c) + 1
                
print(points)

