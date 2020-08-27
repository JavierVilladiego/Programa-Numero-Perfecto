numero = int(input("Por favor digite un numero:  "))

def perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if  numero % i == 0:
             suma += i
    if suma == numero:
        return True 
    else:
        return False

     

if perfecto(numero)==True:
    print("El numero que digito ES PERFECTO" )
else:
  
    print("El numero que digito NO ES PERFECTO")


