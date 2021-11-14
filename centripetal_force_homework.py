# https://pypi.org/project/PySimpleGUI/2.7.0/#:~:text=A%20Text%20Element%20with%20a,is%20(45%2C1)%20.

import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')

layout = [[sg.Text("Enter mass in kilograms"), sg.Input(key='-MASS-', do_not_clear=True, size=(5, 1))],
          [sg.Text("Enter velocity in kilometers per hour"), sg.Input(key='-VELOCITY-', do_not_clear=True, size=(5, 1))],
          [sg.Text("Enter radios in meters"), sg.Input(key='-RADIUS-', do_not_clear=True, size=(5, 1))],
          [sg.Text(size=(10, 1), justification='right', key='-OUT-CALCULATION-'),
           sg.Text(' Newtons')],
          [sg.Button('Calculate', bind_return_key=True), sg.Button('Quit')]
]

window = sg.Window('Calculating Centripetal Force', layout)

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    mass = float(values['-MASS-'])
    velocity = float(values['-VELOCITY-'])
    radius = float(values['-RADIUS-'])
    window['-OUT-CALCULATION-'].Update((mass*(velocity**2))/radius)

window.close()