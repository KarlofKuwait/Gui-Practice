from PySimpleGUI import *
import PySimpleGUI as sg
import time

def RedditBot():

    layout = [
              [sg.Text('Username', size=(15, 1)), sg.InputText('')],
              [sg.Text('Password', size=(15, 1)), sg.InputText('')],
              [sg.Text('Client ID', size=(15, 1)), sg.InputText('')],
              [sg.Text('Client Secret', size=(15, 1)), sg.InputText('')],
              [sg.Text('User Agent', size=(15, 1)), sg.InputText('')],
              [sg.Submit("Log In", size=(15, 1)), sg.Exit()]

    ]

    Login = sg.Window('RedditBot Login').Layout(layout)


    while True:
        event, values = Login.Read()
        if event is None or event == 'Exit':
            break
        if event == "Log In":
            Login.Hide()
            break
    return event, values;

def Start():
    Bot = sg.Window("RedditBot").Layout(layout2)
    while True:
        event, values = Bot.Read()
        if event is None or event == 'Exit':
            break
        if event == "Turn On":
            Bot.Hide()
            break
    return event, values;

    #values = ['Hug_Bot13', 'ForThe1MAn', 'FaVK12dui1rgJw', '12IGnh1EMcmQdDb-A9FJN_gRGuc', 'Hug_Bot13 by /u/Rip2k16']


