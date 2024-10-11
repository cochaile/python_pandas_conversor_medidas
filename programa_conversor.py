import pandas as pd # "Pandas" siempre es necesario para trabajar con archivos excel

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer l archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al Dataframe que sea de pulgadas y se rellene con el cálculo de cm / 2.54

df["pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas) # El método "apply" es de "numpy" que se agregó al instalar pandas 

df.to_excel("medidas_medidas_convertidas.xlsx", index=False) # Creamos un nuevo archivo con las medidas convertidas a partir de nuevo df

print("Conversión completada y guardada en un nuevo archivo excel llamado: 'medidas_medidas_convertidas.xlsx'")