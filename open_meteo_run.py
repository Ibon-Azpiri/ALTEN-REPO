from modulo_open_meteo import tablaAPI,BigQueryLoader

data = tablaAPI().datos()

project_id = 'proyecto1'
table_name = 'DATASET.tabla_meteo'
loader = BigQueryLoader(project_id, table_name)
loader.loader(data)
