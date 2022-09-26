import pandas as pd
from datetime import datetime
import os
now = datetime.now()
current_date = now.strftime("%Y-%B")
date=now.strftime("%d-%m-%Y")

#Tabla unificada con todos los datos

df_museos = pd.read_csv('museos/{}/museos-{}.csv'.format(current_date,date))
df_cines = pd.read_csv('cines/{}/cines-{}.csv'.format(current_date,date))
df_bibliotecas = pd.read_csv('bibliotecas/{}/bibliotecas-{}.csv'.format(current_date,date))
tabla_unificada = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'])

df_museos_dos = df_museos.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
df_cines_dos = df_cines.drop(['Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion',	'Pantallas',	'Butacas',	'espacio_INCAA', 'año_actualizacion'], axis=1)
df_bibliotecas_dos = df_bibliotecas.drop(['Observacion', 'Subcategoria', 'Departamento','Piso', 'Cod_tel', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud','Fuente', 'Tipo_gestion',	'año_inicio',	'Año_actualizacion'], axis=1)

df_museos_dos = df_museos_dos.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_cines_dos = df_cines_dos.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_bibliotecas_dos = df_bibliotecas_dos.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})

tabla_unificada= df_museos_dos
pd.concat([tabla_unificada, df_cines_dos])
pd.concat([tabla_unificada, df_bibliotecas_dos])
new_df=tabla_unificada.assign(fecha_de_carga=date)  #columna nueva con fecha

#Tabla que contiene cines con informacion de provincia, cant de pantallas, cant de butacas, cant de espacios INCAA.

col_prov = df_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].replace('SI', 'si').replace('si', 1)
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].fillna(0)
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].astype("int")
col_prov = col_prov.groupby('Provincia').sum()


#Tabla que con cantidades de: registros totales por categoria, fuente, provincia y categoria.

df_museos_tres = df_museos.drop(['Cod_Loc','IdProvincia','IdDepartamento','Observaciones','subcategoria','localidad','direccion','piso','CP','cod_area','telefono','Mail','Web','Latitud','Longitud','TipoLatitudLongitud','Info_adicional','jurisdiccion','año_inauguracion','actualizacion'], axis=1)
df_cines_tres = df_cines.drop(['Cod_Loc','IdProvincia','IdDepartamento','Observaciones','Departamento','Localidad','Dirección','Piso','CP','cod_area','Teléfono','Mail','Web','Información adicional','Latitud','Longitud','TipoLatitudLongitud','tipo_gestion','Pantallas','Butacas','espacio_INCAA','año_actualizacion'], axis=1)
df_bibliotecas_tres = df_bibliotecas.drop(['Cod_Loc','IdProvincia','IdDepartamento','Observacion','Subcategoria','Departamento','Localidad','Domicilio','Piso','CP','Cod_tel','Teléfono','Mail','Web','Información adicional','Latitud','Longitud','TipoLatitudLongitud','Tipo_gestion','año_inicio','Año_actualizacion'], axis=1)

df_museos_tres = df_museos_tres.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
df_cines_tres = df_cines_tres.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
df_bibliotecas_tres = df_bibliotecas_tres.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})

df_limpia = df_museos_tres
pd.concat([df_limpia, df_cines_tres])
pd.concat([df_limpia, df_bibliotecas_tres])

df_reg_prov = df_limpia.pivot_table(values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)
