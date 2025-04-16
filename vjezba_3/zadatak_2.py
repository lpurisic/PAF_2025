def funkcija(N):
    x = 0
    
    for i in range(N):
        x += 1/3
    
    x = 5 - N * (1/3)
    
    return x

print(funkcija(200))
print(funkcija(2000))
print(funkcija(20000))

#