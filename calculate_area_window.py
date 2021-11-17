import PySimpleGUI as sg
import math

def create():
    # Layout is here because it must be "new" every time you open the window.
    calculate_area_layout = [[sg.Text("Enter radius in centimeters"), sg.Input(key='-RADIUS-', do_not_clear=True, size=(5, 1))],
                [sg.Text(size=(20, 1), justification='right', key='-OUT-AREA-CALCULATION-'),sg.Text(' centimeters squared')],
                [sg.Button('Calculate Area'), sg.Button('Quit')]]

    calculate_area_window = sg.Window("Calculate Circle Area", calculate_area_layout, modal=True)

    while True:
        event, values = calculate_area_window.read()
        if event == "Quit":
            break
        elif event == "Calculate Area":
            float_radius = float(values['-RADIUS-'])
            area = math.pi*(float_radius**2)
            calculate_area_window['-OUT-AREA-CALCULATION-'].update(area)

        
    calculate_area_window.close()