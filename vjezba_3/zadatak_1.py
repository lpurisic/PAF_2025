#a)
#Ocekujem: 5.0 - 4.935 = 0.065

a = 5.0 - 4.935

print(a)

#Koristeci Python dobijem rezultat 0.06500000000000039.
#U memoriji imamo samo 0 i 1, svaki broj moramo pretvoriti u binarni oblik.
#4.935 se ne moze da tocno pretvorit u binarni oblik, pa se mora aproksimirati.
#Ta aproksimacija dovodi do rezultata koji je vrlo blizu 0.065, ali ne sasvim što daje vrijednost poput 0.06500000000000039.

#b)

b = 0.1 + 0.2 + 0.3
print(b)

#Dobili smo 0.6000000000000001 jer Python decimalne brojeve u binarnom obliku zapisuje u dugacke nizove 0 i 1.
#Decimalni brojevi se aproksimiraju, pa aproksimacija daje rezultat koji je priblizan ocekivanom matematickom rezultatu jer je ocekivani rezultat isto decimalni broj.