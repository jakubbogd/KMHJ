# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:09:18 2021
@author: jakub
"""

import PySimpleGUI as sg
import pandas as pd
sg.theme('TealMono')

def read_cities(file):
    data=pd.read_csv(file)
    if list(data.columns.values)!=['city_name','x_coordinate','y_coordinate','commodity']:
        return False
    elif data["x_coordinate"].dtype!="float64" and data["x_coordinate"].dtype!="int64" and data["y_coordinate"].dtype!="float64" and data["y_coordinate"].dtype!="int64":
        return False
    elif len(list(filter(lambda x: x>1000 or x<-1000,data["x_coordinate"])))>0 or len(list(filter(lambda x: x>1000 or x<-1000,data["y_coordinate"])))>0 or len(list(filter(lambda x: x<0,data["commodity"])))>0 or data["commodity"].dtype!="int64":
        return False
    elif any(data.duplicated(subset=["x_coordinate","y_coordinate"])):
        return False
    elif len(data)==0:
        return False
    else:
        return True
    
def read_prod(file):
    data=pd.read_csv(file)
    if list(data.columns.values)!=['city1','city2','travel_time']:
        return False
    elif data["travel_time"].dtype!="float64" and data["travel_time"].dtype!="int64":
        return False
    elif len(list(filter(lambda x: x<=0,data["travel_time"])))>0:
        return False
    elif any(data.duplicated(subset=["city1","city2"])):
        return False
    elif len(data)==0:
        return False
    else:
        for index, row in data.iterrows():
            if row["city1"]==row["city2"]:
                return False
    return True

def read_worker_time(file):
    data=pd.read_csv(file)
    if list(data.columns.values)!=['time']:
        return False
    elif len(data)!=1:
        return False
    elif len(list(filter(lambda x: x<0,data["time"])))>0:
        return False
    else:
        return True

def read_solution(file4,file1):
    data4=pd.read_csv(file4)
    data1=pd.read_csv(file1)
    if list(data4.columns.values)!=['solution']:
        return False
    elif not all(data4["solution"].isin(data1["city_name"])):
        return False
    elif len(data4)==0:
        return False
    else:
        return True
    
def ReadFiles(files):
    if files[3]!="" and (files[0]=="" or files[1]=="" or files[2]==""):
        layout=[[sg.Text("Wczytano tylko rozwiązanie bez pierwotnych plików!")]]
    elif len(list(filter(lambda x: x=="", files)))>1:
        layout=[[sg.Text("Nie wczytano wszystkich plików!")]]
    elif not read_cities(files[0]):
        layout=[[sg.Text("Błędne dane w pliku nr 1")]]
    elif not read_prod(files[1]):
        layout=[[sg.Text("Błędne dane w pliku nr 2")]]
    elif not read_worker_time(files[2]):
        layout=[[sg.Text("Błędne dane w pliku nr 3")]]
    elif files[3]!="" and not read_solution(files[3],files[0]):
        layout=[[sg.Text("Błędne dane w pliku nr 4")]]
    else:
        if files[3]=="":
            del files[3]
        return [pd.read_csv(file) for file in files]
    layout.append([sg.Button("Spróbuj ponownie")])    
    window=sg.Window("Błąd",layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Spróbuj ponownie" or event=="Exit":
            break
    window.close()

def GUI():
    layout=[[sg.Text("Wybierz listę miast:   "),sg.Input(),sg.FileBrowse(key="-IN-")],[sg.Text("Wybierz listę dróg:     "),sg.Input(),sg.FileBrowse(key="-IN2-")],[sg.Text("Wybierz czas:           "),sg.Input(),sg.FileBrowse(key="-IN3-")],[sg.Text("Wybierz rozwiązanie: "),sg.Input(),sg.FileBrowse(key="-IN4-")],[sg.Button("Gotowe")]]
    window=sg.Window("KMHJ - Komiwojażer with GPS",layout,size=(700,350))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Gotowe":
            files=[values["-IN-"],values["-IN2-"],values["-IN3-"]]
            try:
                files.append(values["-IN4-"])
            except FileNotFoundError:
                pass
            ReadFiles(files)
            break
    window.close()
