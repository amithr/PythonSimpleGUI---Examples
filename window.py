# https://pysimplegui.trinket.io/demo-programs#/demo-programs/simple-form
# https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/coin-calculator

import PySimpleGUI as sg
import math

sg.theme("DarkAmber")

layout = [[sg.Text("Calculate volume of sphere")],
          [sg.InputText(key='-NAME-')],
          [sg.InputText(key='-RADIUS-')],
          [sg.Submit(), sg.Cancel()]
]

window = sg.Window('IBDPs first window', layout)

event, values = window.read()

window.close()

def calculate_sphere_volume(radius):
    volume = (4/3)*math.pi*(radius**3)
    return volume

float_radius = float(values['-RADIUS-'])
volume_of_sphere = calculate_sphere_volume(float_radius)

sg.popup("The volume is", volume_of_sphere)

