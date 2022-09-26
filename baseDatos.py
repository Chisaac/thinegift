from sqlalchemy import create_engine
from procesamientoDatos import tabla_unificada, col_prov, df_reg_prov
import psycopg2
#parametros para loguear a la base de datos
user=input("Ingrese su user:")
password=input("Ingrese su password:")
host=input("Ingrese su host:")
puerto=input("Ingrese el puerto:")
base=input("Ingrese la base de datos:")
engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user,password,host,puerto,base))
#Crea tablas si no existen, si existen, se las remplazan
tabla_unificada.to_sql('tabla_unificada', con=engine, if_exists='replace')
col_prov.to_sql('cantidades_cines', con=engine, if_exists='replace')
df_reg_prov.to_sql('categorias_fuentes', con=engine, if_exists='replace')
