# Packages a importer
import os
import sys
import glob
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import xarray as xr
from datetime import datetime,timedelta

# Repertoire ou le fichier se trouve
path_file="C:\\Users\\vazqu\\projet_hm\\pegase_2023_variation_all_watersheds.nc"


# Pour lire le fichier
#print('Reading file: ',path_file)
ds_i = xr.open_dataset(path_file,engine='netcdf4',decode_times=False)
ds_i.close()
#print('Reading file: DONE')
#print(ds_i)
t0=datetime(2023,1,1,0)
tA=timedelta(datetime(2023,2,12,0)-t0)
print(tA)
tB=datetime(2023,3,7,12)+timedelta(hours=6*9)
tC=datetime(2023,3,12,12)+timedelta(hours=6*5)
tD=datetime(2023,9,12,0)+timedelta(hours=6*23)
tE=datetime(2023,12,4,0)+timedelta(hours=6*32)

#Steps a verifier
A= {'time':174,"step":20,"hydro":"GR5j","weather":"ECMWF","watershed":25}
B= {'time':48,"step":9,"hydro":"CEQUEAU","weather":"GFS","watershed":33}
C= {'time':24,"step":5,"hydro":"SIMHYD","weather":"GFS","watershed":42}
D= {'time':132,"step":23,"hydro":"HYMOD","weather":"ECMWF","watershed":3}
E= {'time':192,"step":32,"hydro":"HBV","weather":"HM-WRF","watershed":28}

A_sel = ds_i.sel(A)
B_sel = ds_i.sel(B)
C_sel = ds_i.sel(C)
#D_sel = ds_i.sel(D).to_dataframe
E_sel = ds_i.sel(E)

var=['TObs', 'PObs', 'QObs', 'QForecast']
don=[A_sel,B_sel,C_sel,E_sel]
for donne in don:
    for nom in var:
        
        print(nom,' :',donne[nom].values)
        
print(ds_i["time"].attrs)