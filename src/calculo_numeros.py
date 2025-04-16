# Trabajo Práctico 3: Desarrollo Guiado por Pruebas (TDD) - Manejo de Excepciones.
# Nombre y Apellido: Enzo Agustín Aguirre Polenta.
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
    try:
        numero = int(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")

    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")

    return numero

if __name__ == '__main__':
    try:
        numero = ingrese_numero()
        print(f"Número válido: {numero}")
    except NumeroDebeSerPositivo as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")