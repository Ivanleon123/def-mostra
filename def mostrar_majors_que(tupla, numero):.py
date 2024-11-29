def mostrar_majors_que(tupla, numero):
    """Imprimeix els números de la tupla que són superiors al número donat."""
    print(f"Números majors que {numero}:")
    for num in tupla:
        if num > numero:
            print(num)

# Programa principal
def main():
    # Demanar a l'usuari que introdueixi números enters
    numeros = input("Introdueix números enters separats per espais: ")
    tupla_numeros = tuple(map(int, numeros.split()))  # Convertir l'input en una tupla de enters

    # Mostrar els números majors de 18
    mostrar_majors_que(tupla_numeros, 18)

# Executar el programa
main()