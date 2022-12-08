points = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3,
            },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9,
            },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6,
            }
        }

win = {
        "A": "Y",
        "B": "Z",
        "C": "X"
        }

loose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
        }

draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
        }

def score(p1, p2):
    return points[p1][p2]

def trans(choice, rule):
    if rule == "X":
        return loose[choice]
    elif rule == "Y":
        return draw[choice]
    else:
        return win[choice]

s1 = 0
s2 = 0
for l in open("input.txt"):
    (p1, p2) = l.split()
    s1 += score(p1, p2)
    s2 += score(p1, trans(p1, p2))

print(s1)
print(s2)
