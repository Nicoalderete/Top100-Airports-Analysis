# Proyecto: Análisis de los 100 Aeropuertos Más Transitados

## 📄 Descripción

Este proyecto explora el tráfico aéreo global analizando los 100 aeropuertos más transitados del mundo mediante datos de Kaggle. Se enfoca en descubrir patrones, tendencias y correlaciones en la afluencia de pasajeros, combinando análisis exploratorio, visualización avanzada e inteligencia de datos.

A través de diversas visualizaciones y análisis, se examinan distintos aspectos del tráfico aéreo, incluyendo:

- 📊 **Comparación de tráfico** → Top aeropuertos y países más transitados
- 📉 **Distribución de pasajeros** → Histogramas y tráfico por aeropuerto
- 📌 **Relaciones y patrones** → Correlaciones, clustering y reducción de dimensiones
- 🌍 **Visualización geográfica** → Mapa de calor de aeropuertos y tráfico por país con burbujas
- 🛫 **Interactividad y exploración** → Gráficos dinámicos con Plotly

Además, se documentan los pasos de:
- ✅ **Instalación y configuración del entorno**
- ✅ **Limpieza y transformación de los datos**
- ✅ **Generación de insights mediante técnicas estadísticas y de machine learning**

Este análisis ofrece una visión profunda sobre el comportamiento del tráfico aéreo global, ayudando a entender las dinámicas de la industria aeroportuaria.


---

## 🛠️ Configuración del Entorno y Descarga del Dataset

### 🔹 1. Descripción del Entorno
Verificamos las versiones de Python y la API de Kaggle:
```bash
python3 --version  # Python 3.9.6
kaggle --version   # Kaggle API 1.6.17
```
Si hay problemas con Kaggle, se reinstala:
```bash
pip install --upgrade --force-reinstall kaggle
```

### 🔹 2. Instalación y Configuración de Kaggle API
Configuramos credenciales:
```bash
mkdir -p ~/.kaggle
mv ~/Descargas/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```
Verificamos la configuración:
```bash
kaggle datasets list
```

### 🔹 3. Descarga del Dataset
Descargamos el dataset desde Kaggle:
```bash
cd ~/Documents/Proyectos/Top-100-Airports-Analysis/data
kaggle datasets download -d batrosjamali/top-100-airports-of-the-world -p ./ --unzip
ls -l  # Verificación
```


---

## 🗃️ Limpieza y Transformación de los Datos

### 🔹 4. Creación del script de limpieza
El script `clean_data.py` ejecuta tareas clave:
```python
import pandas as pd

def limpiar_datos(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df['Passengers'] = df['Passengers'].str.replace(',', '').astype(int)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df[['Airport', 'Country', 'Location']] = df[['Airport', 'Country', 'Location']].apply(lambda x: x.str.strip().str.title())
    return df

file_path = "data/Top_100_Airports.csv"
df_cleaned = limpiar_datos(file_path)
df_cleaned.to_csv("data/clean_airports.csv", index=False)
print("\U0001F7E2 Limpieza de datos completada.")
```

Ejecutamos el script:
```bash
python3 notebooks/clean_data.py
```


### 🔹 5. Análisis Exploratorio de Datos (EDA)
En `eda_airports.ipynb`, realizamos un primer análisis del dataset:
```python
import pandas as pd

df = pd.read_csv("data/Top_100_Airports.csv")

print("📌 Dimensiones del dataset:", df.shape)
print("\n📌 Primeras filas del dataset:")
display(df.head())

print("\n📌 Información general:")
df.info()

print("\n📌 Estadísticas descriptivas:")
display(df.describe())

print("\n📌 Valores nulos por columna:")
print(df.isnull().sum())
```


---

## 🔬 Análisis Estadístico y Visualizaciones

Se creó `visualization_airports.ipynb` para generar visualizaciones clave:
- **Top 10 aeropuertos más transitados**.
- **Distribución de pasajeros en aeropuertos**.
- **Países con mayor tráfico aéreo**.

Ejemplo de visualización:
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 aeropuertos
top_airports = df.nlargest(10, 'Passengers')
plt.figure(figsize=(10, 5))
sns.barplot(x='Passengers', y='Airport', data=top_airports, palette='Blues_r')
plt.title("Top 10 Aeropuertos Más Transitados")
plt.xlabel("Número de Pasajeros")
plt.ylabel("Aeropuerto")
plt.show()
```


---

## 🌍 Generación de Coordenadas y Mapa Interactivo

Dentro de `visualization_airports.ipynb`, se usó `geopy` para obtener coordenadas geográficas de los aeropuertos y crear un mapa interactivo.

Ejemplo de generación de coordenadas:
```python
from geopy.geocoders import Nominatim

def obtener_coordenadas(aeropuerto, pais):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(f"{aeropuerto}, {pais}")
    if location:
        return location.latitude, location.longitude
    return None, None
```

---

- Los datos se guardaron en `clean_airports_with_coordinates.csv` y se usaron en un mapa interactivo con `folium`.

- Se creó una carpeta llamada `imgs` para almacenar las capturas de pantalla de las visualizaciones creadas para su posterior uso. 

- Se generó ademas un archivo llamado `visualizations.md` con el objetivo de mostrar las visualizaciones generadas de manera ordenada y prolija, prescindiendo del script base. 

- Se creó la carpeta contenedora `reporting` con el objetivo de almacenar el archivo final de reporte. 

- Por ultimo, se creó el arhivo final `Storytelling.md` con el objetivo de reportar los insights logrados para las partes interesadas. 


---


## 📚 Estructura del Proyecto
```bash
Top-100-Airports-Analysis/
│── data/  
│   ├── clean_airports_with_coordinates.csv  
│   ├── clean_airports.csv  
│   ├── Top_100_Airports.csv  
│── reporting/
│   ├── Storytelling.md
│── notebooks/  
│   ├── clean_data.py  
│   ├── eda_airports.ipynb 
│── visualizations/  
│   ├── imgs/
│   ├── mapa_calor_aeropuertos.html 
│   ├── visualization_airports.ipynb  
│   ├── visualizations.md
│── README.md  
│── requirements.txt

```


---

## 🔗 Referencias
- [Kaggle API: Documentación Oficial](https://www.kaggle.com/docs/api)
- [Dataset: Top 100 Airports of the World](https://www.kaggle.com/datasets/batrosjamali/top-100-airports-of-the-world)