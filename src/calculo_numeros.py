from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero() -> int:
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    numero = int(entrada)  # No se maneja ValueError
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")
    return numero

if __name__ == '__main__':
    numero = ingrese_numero()
    print(f"Número válido: {numero}")