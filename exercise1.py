def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = ((EK/AK_abs**(1/t_abs)-1))# * 100
    return cagr
cagr_berechnung(100, 700, 30)

print(cagr_berechnung(100, 700, 30)
      