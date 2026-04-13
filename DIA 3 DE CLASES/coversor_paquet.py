import pandas as pd

data = [
    {"nombre": "Ana", "edad": 20, "ciudad": "Guatemala"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Quetzaltenango"},
    {"nombre": "Marta", "edad": 30, "ciudad": "Escuintla"},
]

df = pd.DataFrame(data)

df.to_parquet("usuarios_prueba.parquet")