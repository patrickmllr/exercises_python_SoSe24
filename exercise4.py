quad_zahl =[]
for i in range ( [1,11):
    if i % 2 == 1: #prüfen ob Zahl ungerade
        quad_zahl.append(i ** 2)
    else:
        quad_zahl.append(i)

print(quad_zahl)

 
import matplotlib.pyplot as plt
def geometric_series_sum(a, r, n):
    s_n =  []
    sum = 0
    for i in range(0, n):
        sum += a * (r ** i)
        s_n.append(sum)
    return sum
# Testen der Funktion
a = 1   # Erster Term
r = 0.5  # Verhältnis
n = 10  # Anzahl der Terme
result = geometric_series_sum(a, r, n)
print("Die Summe der ersten", n, "Terme der geometrischen Reihe beträgt:", result)
plt.plots(s_n)
   



