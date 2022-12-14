letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = 0

for data in open("input.txt"):
    lines = data.splitlines()
    for l in lines:
        m = len(l) // 2
        firstHalf, secondHalf = l[:m], l[m:]
        for c in firstHalf:
            if c in secondHalf:
                points += letters.find(c) + 1
                break
                
print(points)



        
