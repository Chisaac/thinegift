import requests
import os
from datetime import datetime
now = datetime.now()
current_date = now.strftime("%Y-%B")
date=now.strftime("%d-%m-%Y")

#Los archivos se descargan y se crean archivos con los nombres normalizados.
museos = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRMw4sa6DpyNUvttaOnlGhlMjAo3LzWYLgTdITK1PkiCmT7KhJhiqIy1bkl1A_sq_p9suvkwq0qv2qx/pub?output=csv", allow_redirects = True)
os.makedirs('museos/{}'.format(current_date))
open('museos/{}/museos-{}.csv'.format(current_date,date), 'wb').write(museos.content)

cines = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRMVMDwpwHh_PVIrin7erx1_OM4hsvzYwBqCLOs4iWgmj99IyDePNEuaEEi0yGEZTX-v9R4hp1NSjNH/pub?output=csv", allow_redirects= True)
os.makedirs('cines/{}'.format(current_date))
open('cines/{}/cines-{}.csv'.format(current_date,date), 'wb').write(cines.content)

bibliotecas = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRdr0XGdvzJZtU7aPSAPKGVHz5KMDS3f-Y42WyyfbUH3LLr_6FjL7Kp4oDzvKToBB6jyrLjtx1t2BOl/pub?output=csv", allow_redirects = True)
os.makedirs('bibliotecas/{}'.format(current_date))
open('bibliotecas/{}/bibliotecas-{}.csv'.format(current_date,date), 'wb').write(bibliotecas.content)
