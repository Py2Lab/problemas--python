#1. una funcion que reciba una edad y nos diga si somos mayores de edad o no

def es_mayor_de_edad(edad: int) -> bool:
    if(edad >= 18):
        #Si se cumple la condicion entramos aqui
        return True
    else:
        #En cualquier otro caso entramos aqui
        return False
    #return True if edad >= 18 else False

#2. escribir una funcion que reciba dos numero dividendo y divisor, si el divisor es 0 mostrar
# error en otro caso mostrar el resultado de la division

def dividir(dividendo: float, divisor: float) -> float or str:
    if(divisor == 0):
        return "Error el divisor es 0"
    else:
        resultado: float = dividendo/divisor
        return resultado

#Una funcion que dado una lista nos devuleva otra lista diciendonos si los numeros en su posicion son pares o impares
# [1,2,3] -> ["impar", "par","impar"]

def es_par_impar(numero: int) -> str:
    if(numero % 2 == 0):
        return "par"
    else:
        return "impar"

def lista_pares_impares(lista_numeros: list) -> list:
    lista_de_cadenas: list= []
    for numero in lista_numeros:
        lista_de_cadenas.append(es_par_impar(numero))
    return lista_de_cadenas

#Funcion que imprima 10 veces cualquier numero que le pasemos
def imprime_diez(numero: int) -> None:
    #variable
    i: int = 0
    while(i < 10):
        #Transformamos de un int a un str
        print(str(numero))
        #"En asignaciones siempre se evalua lo de la derecha del simbolo = primero y luego se asigna a la variable
        i = i + 1
    
#Funcion que imprima la tabla de multiplicar de cualquier numero del 1 al 10
# tabla_multiplicar(1) ->
# 1 x 1 = 1
# 1 x 2 = 2
# .........
# 1 x 10 = 10

def tabla_multiplicar(numero: int) -> None:
    i: int = 1
    while( i <= 10):
        print(str(numero) + " x " + str(i) + " = " + str(numero*i))
        i = i + 1


