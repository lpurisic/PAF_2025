import math

brojevi = []
n = 10

#a)
for i in range (n):
    broj = float(input('Unesi neki broj: '))
    
    brojevi.append(broj)

ar_sr = sum(brojevi) / len(brojevi)

stand_dev = math.sqrt(sum((x - ar_sr)**2 for x in brojevi) / n*(n-1))

print(ar_sr)
print(stand_dev)

#b)
import statistics

arit_sr = statistics.mean(brojevi)
st_dev = statistics.stdev(brojevi)

print(arit_sr)
print(st_dev)