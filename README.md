Para runnear el challenge debe:

1- En el command prompt instalar:

pip install virtualenv

2- En el directorio ejecutar:

virtualenv nombredelentorno

3- Activar entorno virtual:

.\nombredelentorno\Scripts\activate

4- Instalar:

pip install pandas
pip install SQLAlchemy
pip install requests
pip install python-decouple

5- En ese entorno virtual y trabajando en la carpeta del proyecto, ejecutar:

python extraccionDatos.py

python procesamientoDatos.py

python baseDatos.py
