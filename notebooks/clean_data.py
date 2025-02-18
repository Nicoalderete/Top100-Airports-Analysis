import pandas as pd

def limpiar_datos(file_path):
    """
    Realiza la limpieza del dataset de aeropuertos.
    
    Pasos:
    1. Elimina espacios en nombres de columnas.
    2. Convierte la columna 'Passengers' a tipo numérico.
    3. Elimina duplicados.
    4. Maneja valores nulos.
    5. Normaliza el texto en columnas categóricas.
    """
    
    # 🔹 Carga del dataset
    df = pd.read_csv(file_path)

    # 🔹 Limpiar nombres de columnas
    df.columns = df.columns.str.strip()

    # 🔹 Conversion la columna "Passengers" a tipo numérico
    df['Passengers'] = df['Passengers'].str.replace(',', '').astype(int)

    # 🔹 Eliminar duplicados
    df = df.drop_duplicates()

    # 🔹 Manejo de valores nulos
    df = df.dropna()

    # 🔹 Normalizar texto en columnas categóricas
    df['Airport'] = df['Airport'].str.strip().str.title()
    df['Country'] = df['Country'].str.strip().str.title()
    df['Location'] = df['Location'].str.strip().str.title()

    return df

# 🔹 Especificar la ruta del archivo CSV
file_path = "../data/Top 100 Bussiest Airports in the World - Sheet2.csv"

# 🔹 Ejecutar la función de limpieza y guardar el dataset limpio
df_cleaned = limpiar_datos(file_path)

# 🔹 Guardar el nuevo dataset limpio
df_cleaned.to_csv("../data/clean_airports.csv", index=False)

print("✅ Limpieza de datos completada. Archivo guardado como 'clean_airports.csv'.")
