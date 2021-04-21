# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:09:18 2021

@author: jakub
"""

import PySimpleGUI as sg
import os.path

sg.theme('TealMono')


def Wczytaj():
    layout=[[sg.Text("Wybierz listę miast:   "),sg.Input(),sg.FileBrowse(key="-IN-")],[sg.Text("Wybierz listę dróg:     "),sg.Input(),sg.FileBrowse(key="-IN2-")],[sg.Text("Wybierz czas:           "),sg.Input(),sg.FileBrowse(key="-IN3-")],[sg.Text("Wybierz rozwiązanie: "),sg.Input(),sg.FileBrowse(key="-IN4-")],[sg.Button("Gotowe")]]
    window=sg.Window("KMHJ - Komiwojażer with GPS",layout,size=(700,350))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Gotowe":
            files=[values["-IN-"],values["-IN2-"],values["-IN3-"],values["-IN4-"]]
            break
    return files


files=Wczytaj()
print(files)
