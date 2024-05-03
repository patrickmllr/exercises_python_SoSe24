import matplotlib.pyplot as plt

def spar_funktion(AK, SR, i, lz):
    kapital = AK
    gesamt_kapital = []
  
    for k in range(1, lz+1):
       kapital = SR + kapital * (1+i)
       gesamt_kapital.append(kapital)
       
       return gesamt_kapital
        
end_kapital = spar_funktion (AK = 10000, SR = 1000, i = 0.01, lz = 10)



plt.bar(range(1,11), end_kapital)

   