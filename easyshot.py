import os
import pyscreenshot as ImageGrab
import PySimpleGUIQt as sg

sg.theme('Reddit')  # Add some color to the window

layout = [
    [sg.InputText('Enter Name', key='input_name')],
    [sg.Button('Take Screenshot')], ]

def takeScreenshot ():
    im = ImageGrab.grab()
    im.save(f'{name}.png')

window = sg.Window('EasyShot', layout)
event, values = window.Read()

if event == 'Take Screenshot':
    name = values['input_name']
    takeScreenshot()

