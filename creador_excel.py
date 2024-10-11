import pandas as pd # Utilizamos un acrónimo (siempre se hece así)

# Dataframe es la información básica de las piezas y centímetros  para poder armar el excel

data = {
    "piezas:": ["Pata","Tablero","Puerta","Estante","Panel Lateral"],
    "Centimetros": [40,120,60,30,180]
}

df = pd.DataFrame(data) # Estoy creando el Dataframe en la variable df

# Guardar el Dataframe en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)