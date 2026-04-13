import csv
import json
import pandas as pd

def leer_csv(ruta):
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # DictReader convierte el CSV en una lista de diccionarios
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        return "Error: No se encontró nombres.csv"

def leer_json(ruta):
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # json.load convierte el JSON en una lista/diccionario de Python
            return json.load(archivo)
    except FileNotFoundError:
        return "Error: No se encontró productos_combinados.json"

def leer_parquet(ruta):
    try:
        # pd.read_parquet es la función de Pandas para este formato
        return pd.read_parquet(ruta)
    except FileNotFoundError:
        return "Error: No se encontró usuarios_prueba.parquet"

# PRACTICA

print("--- PROCESANDO DATOS REALES (DÍA 3) ---")


nombres = leer_csv('nombres.csv')
print("\nRegistros de nombres.csv:")
print(nombres)


productos = leer_json('productos_combinados.json')
print("\nPrimeros 2 productos del JSON:")
print(productos[0:2])


usuarios = leer_parquet('usuarios_prueba.parquet')
print("\nVista previa del archivo Parquet:")
print(usuarios)