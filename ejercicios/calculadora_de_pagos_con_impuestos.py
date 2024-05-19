""" Este programa toma como alrgumentos 2 parámetros, el pago sin impuesto y el impuesto valorado en porcentajes
luego hace los cálculos correspondientes y le añade el pago total al operario
"""

def Calcula_Con_Impuesto(pago_Sin_Impuesto, porciento):
    pago_Total = pago_Sin_Impuesto / 100 * porciento 
    return pago_Total

print(Calcula_Con_Impuesto(1000, 7.5))