## Vreated by Wyctor Fogos da Rocha, 28/11/2021 - Évry - France
from datetime import datetime
import pywifi
import time
import keyboard
import numpy as np
import pandas as pd


X=[0]
Y=[0]
Z=[0]
Ssid=[]
Bssid=[]
Signal=[]
x_aux=0
y_aux=0
z_aux=0


def write_dataset(x,y,z,ssid,bssid,signal):
    ### Clear the first values
    del x[0]
    del y[0]
    del z[0]
    ##Prepare data to be saved
    df = pd.DataFrame({'X': x,
                   'Y': y,
                   'Z': z,
                   'Wifi-Ssid':ssid,'Wifi-Bssid':bssid,'Wifi-Signal':signal})
    print(df)
    df.to_csv('DATASET_WIFI_POINTS_{}.csv'.format(time.time()),index=True, header=True)
    x=[0]
    y=[0]
    z=[0]
    ssid=[]
    bssid=[]
    signal=[]
    return x, y, z,ssid,bssid,signal

while True:
    ##Try to connect with the wifi's module
    try:
        ##Search for wifi's networks
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(0.5)
        results = iface.scan_results()

        ##For each wifi point, the program save each one
        for i in range(len(results)):
            print(results[i].ssid, results[i].bssid, results[i].signal)
            Ssid.append(results[i].ssid)
            Bssid.append(results[i].bssid) 
            Signal.append(results[i].signal)
            X.append(x_aux)
            Y.append(y_aux)
            Z.append(z_aux)
            print("Auxiliar X:{}, Y:{} et Z:{}".format(X[-1],Y[-1],Z[-1]))
      
        ##Stop the aquisition process and change the references
        if keyboard.is_pressed('p'):
            x_aux=float(input("X position:"))
            y_aux=float(input("Y position:"))
            z_aux=float(input("Z position:"))
            print("Nouvelles valeurs des X:{}, Y:{} et Z:{}".format(x_aux,y_aux,z_aux))

        ## Verify the 'Keyboard' and over the process
        elif keyboard.is_pressed('q'):
            ##Write all data in a .csv file and over the program
            X, Y, Z,Ssid,Bssid,Signal=write_dataset(X,Y,Z,Ssid,Bssid,Signal)
            print(X, Y, Z,Ssid,Bssid,Signal)
            print("-------------------------")
            break
    # if isn't possible to verify the wifi's connection
    except:
        print("Impossible to scan networks!")
        break