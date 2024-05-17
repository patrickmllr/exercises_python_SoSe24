a = 1
r = 0.5
s = 0
k = 0
grenzwert = 1/(1-r)
epsilion = 0.0001
while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    if (grenzwert - s) < epsilion:
        break
        