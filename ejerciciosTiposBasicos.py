#1. Imprimir la cadena "HOLA MUNDO"

def imprimir_hola_mundo():
    print("HOLA MUNDO")
    
#2. Guardar en una variable la cadena HOLA MUNDO e imprimirla





def imprimir_hola_mundo_2():
    #variable cadena
    cadena = "HOLA MUNDO"
    print(cadena)
    
#3. definrir una funcion que pida el nombre y devuelva Hola + nombre ej: Hola juan

def saluda(nombre: str):
    hola: str = "Hola"
    #Concatenando dos strings
    print(hola + nombre)
    
#4. calcula la siguiente operacion ((1000+1)*200/6)

def resuelve_operacion():
    #El lenguaje de programacion ya calcula las operaciones numericas
    resultado: float = (((1000+1)*200)/6)
    print(resultado)
    
#5. Funcion que reciba horas y coste de horas e imprima la paga

def calcula_paga(horas: float, coste_por_hora: float):
    pago: float = horas * coste_por_hora
    print(pago)
    
#6. funcion que calcule la siguiente operacion (n(n+1))/2 donde n es cualquier numero
#Nota la formula calcula la suma de los primeros n numeros enteros
# 1 + 2 + 3 + 4 + 5 = (5(5+1))/2

def suma_primeros_n_numeros(numero: int):
    resultado: int = (numero*(numero+1))/2
    print(resultado)
    
#7. calcula el indice de masa corporal la formula es kg/ estatura^2
# a^b es igual a a*a*a*a... b veces
#a^2 es igual a*a

def calcula_imc(kg: float, estatura: float):
    imc: float= (kg)/(estatura*estatura)
    print("Tu masa de imc es: " + str(imc))
    
#8 imrpime el restatnte de una division de dos numeros enteros

def devuelve_el_resto(numero_a: int, numero_b:int):
    #Modulo regresa el restantde de una division 
    restante: int = numero_a / numero_b
    #format remplaza sus parametros por los {} dentro del string
    print("La division de {} con {} da un resntante de {}".format(numero_a, numero_b, restante))

#9. funcion que pregunte el nombre y un numero de saludos y te salude ese numero de veces
# ej.
# Alexis, 2
# Hola, alexis
# Hola, alexis

def saluda_n_veces(nombre: str, numero_saludos: int):
    #Repite bloques de codigo en el tantas veces como la condicion se cumpla
    #while(condicion) donde condicion es verdadera o falsa
    numero_de_iteraciones: int = 0
    while(numero_de_iteraciones < numero_saludos):
        # Bloque de codigo
        print("Hola " + nombre)
        numero_de_iteraciones = numero_de_iteraciones + 1
        
