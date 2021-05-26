# -*- coding: utf-8 -*-
"""
files.py
==========
Moduł odpowiedzialny za interfejs graficzny.
"""

import PySimpleGUI as sg
import pandas as pd
sg.theme('TealMono')

def read_cities(file):
    """
    Funkcja sprawdza poprawność pliku z listą miast.
    :param file: Ścieżka do pliku z listą miast
    :return: True, jeśli dane poprawne. W przeciwnym wypadku False
    """
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
    
def read_prod(file,file1):
    """
    Funkcja sprawdza poprawność pliku z listą dróg.
    :param file: Ścieżka do pliku z listą dróg
    :return: True, jeśli dane poprawne. W przeciwnym wypadku False
    """
    data=pd.read_csv(file)
    data1=pd.read_csv(file1)
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
    elif not check_cities(data,data1):
        return False
    else:
        for index, row in data.iterrows():
            if row["city1"]==row["city2"]:
                return False
    return True

def read_worker_time(file):
    """
    Funkcja sprawdza poprawność pliku z czasem sprzedawcy.
    :param file: Ścieżka do pliku z czasem sprzedawcy
    :return: True, jeśli dane poprawne. W przeciwnym wypadku False
    """
    data=pd.read_csv(file)
    if list(data.columns.values)!=['time']:
        return False
    elif len(data)!=1:
        return False
    elif len(list(filter(lambda x: x<0,data["time"])))>0:
        return False
    else:
        return True

def read_solution(file4,file1,file2):
    """
    Funkcja sprawdza poprawność pliku z rozwiązaniem.
    :param file: Ścieżka do pliku z rozwiązaniem
    :return: True, jeśli dane poprawne. W przeciwnym wypadku False
    """
    data4=pd.read_csv(file4)
    data1=pd.read_csv(file1)
    data2=pd.read_csv(file2)
    if list(data4.columns.values)!=['solution']:
        return False
    elif not all(data4["solution"].isin(data1["city_name"])):
        return False
    elif len(data4)==0:
        return False
    elif check_country_roads(data4,data2):
        return False
    else:
        return True
    
def ReadFiles(files):
    """
    Funkcja sprawdza poprawność podanych plików. Pokazuje komunikat w razie błędnego pliku.
    :param files: Ścieżki do plików pokolei z listą miast, listą dróg, czasem sprzedawcy i rozwiązaniem
    :return: Jeśli dane są poprawne, zwraca listę złożoną z ramek danych z plików wejściowych. W przeciwnym wypadku zwraca false
    """
    if files[3]!="" and (files[0]=="" or files[1]=="" or files[2]==""):
        layout=[[sg.Text("Wczytano tylko rozwiązanie bez pierwotnych plików!")]]
    elif len(list(filter(lambda x: x=="", files)))>1:
        layout=[[sg.Text("Nie wczytano wszystkich plików!")]]
    elif not read_cities(files[0]):
        layout=[[sg.Text("Błędne dane w pliku nr 1")]]
    elif not read_prod(files[1],files[0]):
        layout=[[sg.Text("Błędne dane w pliku nr 2")]]
    elif not read_worker_time(files[2]):
        layout=[[sg.Text("Błędne dane w pliku nr 3")]]
    elif files[3]!="" and not read_solution(files[3],files[0],files[1]):
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
    return False

def GUI():
    """
    Funkcja umożliwia interakcje użytkownika z aplikacją. Umożliwia także ponowne wprowadzenie danych.
    :return: Ramki danych otrzymane z plików podanych przez użytkownika.
    """
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
            dfs = ReadFiles(files)
            if dfs==False:
                continue
            break
    window.close()
    return dfs

def Error(text):
    """
    Funkcja tworząca komunikat z daną treścią o błędzie.
    :param text: Tekst z błędem do wyświetlenia
    """
    layout=[[sg.Text(text)],[sg.Button("OK")]]
    window=sg.Window("KMHJ - Komiwojażer with GPS",layout,size=(350,125))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit" or event=="OK":
            break
    window.close()
    
def Save(result):
    """
    Funkcja zapisująca rozwiązanie problemu do pliku csv.
    :param result: Ramka danych z rozwiązaniem do zapisania
    """
    layout=[[sg.Text("Wybierz lokalizację dla rozwiązania"),sg.Input(),sg.FolderBrowse(key="-IN-")],[sg.Button("Gotowe")]]
    window=sg.Window("KMHJ - Komiwojażer with GPS",layout,size=(700,200))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event=="Gotowe":
            path=values["-IN-"]
            break
    window.close()
    result.to_csv(str(path)+"/solution.csv", index=False)
    
def check_country_roads(sol,roads):
    """
    Funkcja sprawdzająca czy w pliku z rozwiązaniem są tylko odpowiednie miasta.
    :param sol: Ramka danych z rozwiązaniem
    :param roads: Ramka danych z listą dróg
    :return: False, jeśli wszystkie drogi z sol znajdują się w roads. True w przeciwnym wypadku
    """
    roads=[[roads.loc[:,"city1"][i],roads.loc[:,"city2"][i]] for i in range(len(roads))]
    roads_sol1=[[sol.loc[i,"solution"],sol.loc[i+1,"solution"]] for i in range(len(sol)-1)]
    roads_sol2=[[sol.loc[i+1,"solution"],sol.loc[i,"solution"]] for i in range(len(sol)-1)]
    return not all([roads_sol1[i] in roads or roads_sol2[i] in roads for i in range(len(roads_sol2))])


def check_cities(roads, cities):
    """
    Funkcja sprawdzająca czy w pliku z rozwiązaniem są tylko odpowiednie miasta.
    :param roads: Ramka danych z listą dróg
    :param cities: Ramka danych z listą miast
    :return: True, jeśl w roads są miasta tylko z cities. WPP False
    """
    roads1=[roads.loc[:,"city1"][i] for i in range(len(roads))]
    roads2=[roads.loc[:,"city2"][i] for i in range(len(roads))]
    cities=[cities.loc[:,"city_name"][i] for i in range(len(cities))]
    if len([el for el in roads1 if el not in cities])>0:
        return False
    elif len([el for el in roads2 if el not in cities])>0:
        return False
    else:
        return True
