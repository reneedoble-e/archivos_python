# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv

    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---

def altura_promedio(objetivo):
    with open('alturas.csv', mode='r') as csvfile: # with open cierra automaticamente el archivo
        data = list(csv.DictReader(csvfile))
    valor = 0
    contador = 0
    for fila in data:
        if fila.get('genero') == objetivo:
            valor += float(fila.get('altura', 0.0)) # trayendo el nombre de la clave para hacer numeros de string a decimales
            contador += 1
    promedio = valor / contador        
    return promedio

if __name__ == '__main__':
    genero = str(input('Ingrese el nombre del genero: ')).lower()
    promedio = altura_promedio(genero)
    print(f'El promedio de altura para {genero} es {promedio}')