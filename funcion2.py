def Alonso_Estrella():
    """
    Dibuja una estrella de cinco puntas en la consola.
    La “estrella” es una lista de cadenas; cada elemento representa una fila.
    """
    estrella = [
        "    *    ",
        "   * *   ",
        "  *****  ",
        " *     * ",
        "*       *"
    ]
    
    # Recorremos la lista imprimiendo cada línea
    for fila in estrella:
        print(fila)


# Ejemplo de uso
if __name__ == "__main__":
    Alonso_Estrella()