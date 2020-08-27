def perfecto():
    numero = int(input("Por favor digite un numero:  "))
    suma = 0
    for i in range(1, numero):
        if  numero % i == 0:
             suma += i
    if suma == numero:
        print("El numero digitado ES PERFECTO")
    else:
        print("El numero digitado NO ES PERFECTO")

    return 

def main():
    perfecto()

if __name__ == "__main__":
    main()
    