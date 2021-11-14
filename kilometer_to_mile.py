# https://pypi.org/project/PySimpleGUI/2.7.0/#:~:text=A%20Text%20Element%20with%20a,is%20(45%2C1)%20.

import PySimpleGUI as sg

sg.change_look_and_feel('GreenTan')

layout = [[sg.Text("Enter distance in kilometers"), sg.Input(key='-KILO-', do_not_clear=False, size=(5, 1))],
          [sg.Text(size=(5, 1), justification='right', key='-OUT-KM-'),
          sg.Text('km= '),
          sg.Text(size=(5, 1), key='-OUT-MI-'),
          sg.Text('miles')],
          [sg.Button('Convert'), sg.Button('Quit')]
]

window = sg.Window('Kilometer Conversion', layout)

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    window['-OUT-KM-'].Update(values['-KILO-'])
    window['-OUT-MI-'].Update(float(values['-KILO-'])*0.6214)

window.close()