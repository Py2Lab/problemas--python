def zodiaco(numero: int) -> str:
    if numero == 1 :
        return "tu signo es capricornio"
    elif numero == 2 :
        return "tu signo es acuario"
    elif numero == 3 :
        return "tu signo es pisis"
    elif numero == 4 :
        return "tu signo es aries"
    elif numero == 5 :
        return "tu signo es tauro"
    elif numero == 6 :
        return "tu signo es geminis"
    elif numero == 7 :
        return "tu signo es cancer"
    elif numero == 8 :
        return "tu signo es leo"
    elif numero == 9 :
        return "tu signo es virgo"
    elif numero == 10 :
        return "tu signo es libra"
    elif numero == 11 :
        return "tu signo es escorpio"
    elif numero == 12 :
        return "tu signo es sagitario"
    else:
        return "ingresa un numero del 1 al 12"

print(zodiaco(6))

def operaciones(numero_a: float, numero_b: float, operacion: str) -> float or str:
    if operacion == "+" :
        return numero_a + numero_b
    elif operacion == "-" :
        return numero_a - numero_b
    elif operacion == "*" :
        return numero_a * numero_b
    else:
        return "ingrese una operacion valida"

print(str(operaciones(5, 8, "-")))