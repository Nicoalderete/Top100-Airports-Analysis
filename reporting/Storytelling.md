## El Pulso del Tráfico Aéreo Global

En un mundo cada vez más conectado, los aeropuertos no solo son infraestructuras de tránsito, sino auténticos nodos del comercio, el turismo y la economía global. Sin embargo, ¿cuáles son los aeropuertos que dominan el tráfico aéreo? ¿Cómo se distribuyen los pasajeros en distintas regiones del mundo? Y lo más importante, ¿qué patrones subyacentes revelan estos datos?

Para responder estas preguntas, analizamos los 100 aeropuertos más transitados del mundo, combinando datos de tráfico de pasajeros, análisis estadístico y visualizaciones avanzadas para revelar los secretos detrás del flujo aéreo global.

Comenzamos identificando los aeropuertos con mayor afluencia de pasajeros. Un gráfico de barras revela que aeropuertos como Atlanta (ATL), Beijing (PEK) y Dubai (DXB) encabezan la lista, con más de 80 millones de pasajeros anuales cada uno. Esta concentración de tráfico no es casualidad:

✅ Atlanta actúa como el principal hub de conexión de EE.UU.

✅ Beijing representa la creciente demanda del mercado asiático.

✅ Dubai se consolida como el centro estratégico del tráfico entre Europa, Asia y África.

<img src="./visualizations/imgs/Top10_Aeropuertos.png" alt="Top 10 Aeropuertos" width="70%">

Luego, algo interesante que podemos notar es la clara desigualdad entre la mayoría de los aeropuertos(quienes manejan un tráfico considerablemente menor) con los gigantes del sector. Mientras los 10 aeropuertos más transitados concentran gran parte del flujo aéreo, existe un largo tail de aeropuertos con tráfico significativamente menor.

<img src="./visualizations/imgs/Distribucion_pasajeros.png" alt="Distribución Pasajeros" width="70%">


De estos gigante del sector, encontramos que es Estados Unidos quién lidera el tráfico mundial, con más de 10 aeropuertos en el top 100 y un volumen de pasajeros que duplica al del segundo país en la lista.

<img src="./imgs/Top10_paises_trafico.png" alt="Top 10 Países" width="70%">


Descubrimos además, que factores como la ubicación geográfica y la categoría del aeropuerto pueden influir en su volumen de tráfico.

<img src="./imgs/Correlaciones.png" alt="Mapa de Calor" width="40%">

Para profundizar, aplicamos un clustering con K-Means, agrupando aeropuertos según similitudes en su tráfico y ubicación.

<img src="./imgs/Clustering.png" alt="Clustering" width="40%">


Para cerrar nuestro análisis, utilizamos un mapa de calor interactivo que nos muestra la concentración de tráfico aéreo en el mundo. Como era de esperar, vemos un fuerte resplandor en América del Norte, Europa y Asia, mientras que regiones como África y América del Sur tienen una menor densidad de tráfico.

<img src="./imgs/Mapa_calor.png" alt="Mapa de Calor" width="70%">


## 📌 Conclusiones y Reflexión Final

Este análisis nos permite extraer varias conclusiones clave:

🚀 El tráfico aéreo está altamente concentrado en unos pocos aeropuertos y países.

🌎 Los hubs globales actúan como puntos de conexión clave para millones de pasajeros.

📈 El crecimiento del tráfico aéreo en Asia y Medio Oriente redefine la conectividad global.

📊 El clustering y el análisis de correlación ayudan a entender los patrones del sector.

Este estudio no solo nos ayuda a comprender la distribución actual del tráfico aéreo, sino que también puede ser utilizado para prever tendencias futuras en la industria de la aviación.

