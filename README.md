# ALTEN-REPO
Repositorio con los ejercicios de la prueba técnica de ALTEN.

### EJERCICIO 1
Para el desarrollo del primer ejercicio se han descargado datos horarios de temperatura en la superficie, módulo de viento a 10m y húmedad relativa de la API pública de Open Meteo para tres ubicaciones: Barcelona, Madrid y Berriz.

El fichero modulo_open_meteo.py contiene las funciones que se ocupan de descargar los datos de la API y cargarlos en una tabla de BigQuery. Para poder cargar los datos mediante pandas_gbq es necesario autentificarse mediante una cuenta de Google.

Estas funciones se ejecutan mediante el programa open_meteo_run.py

Por último, se ha desarrollado una consulta (consulta_bq.sql) que genera una nueva tabla aplicando varias transformaciones a la tabla original. Esta consulta se centra en los valores de temperatura diarios para ubicación. De este modo, calcula el valor máximo diario de temperatura para ubicación y, mediante una función de ventana, compara el valor diario con el del día anterior, calculando la diferencia.

### EJERCICIO 2
Para el segundo ejercicio se ha creado un dag que orquesta los procesos de descarga de los datos, carga en BigQuery y ejecución de una consulta SQL para la transformación de la tabla.

Tanto la función de Python como la consulta que automatiza el dag se encuentran en el directorio funciones_dag. Este dag se encarga de automatizar los procesos de descarga de datos, carga en BigQuery y transformación definidos en el ejercicio 1.


NOTA: Por falta de tiempo no ha sido posible instalar todas las dependencias (crear una cuenta de Google Cloud con BigQuery y Airflow), de modo que no se han insertado capturas del proceso, ya que no ha sido posible llevar a cabo en la práctica.

