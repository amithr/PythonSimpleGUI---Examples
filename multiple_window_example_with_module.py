import PySimpleGUI as sg
import calculate_area_window
import math

sg.change_look_and_feel('DarkAmber')

layout = [[sg.Text("Enter radius in centimeters"), sg.Input(key='-RADIUS-', do_not_clear=True, size=(5, 1))],
          [sg.Text(size=(20, 1), justification='right', key='-OUT-CALCULATION-'),
           sg.Text(' centimeters squared')],
          [sg.Button('Calculate Volume'), sg.Button('Calculate Area'), sg.Button('Quit')]
]

window = sg.Window('Calculate Sphere Volume', layout, size=(500, 100))

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    elif event == 'Calculate Volume':
        radius = float(values['-RADIUS-'])
        volume = (4/3)*math.pi*(radius**3)
        print(volume)
        window['-OUT-CALCULATION-'].Update(volume)
    elif event == 'Calculate Area':
        calculate_area_window.create()

window.close()