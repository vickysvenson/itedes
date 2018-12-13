def exponenciar (base,exponente):
    resultado = base
    for i in range(1, exponente):
        resultado = resultado * base
    return resultado

base = int(input("base: "))
exponente = int(input("exponente: "))
resultado = exponenciar(base,exponente)
print(resultado)
