import PySimpleGUI as sg

# Future Tutorial - https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0

sg.theme('Black')

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter your passport number:"), sg.Input(key='-PASSPORT_NUMBER-', do_not_clear=True, size=(10, 1))],
          # "RADIO" makes the radio buttons part of the same group, so when you click one, the other will be unchecked
          [sg.Radio("Male", "RADIO", key='-MALE-'), sg.Radio("Female", "RADIO", key='-FEMALE-')],
          [sg.Input(key='-DEPARTURE-', size=(20,1)), sg.CalendarButton("DATE OF DEPARTURE", close_when_date_chosen=True,  target='-DEPARTURE-', location=(0,0), no_titlebar=False )],
          [sg.Input(key='-ARRIVAL-', size=(20,1)), sg.CalendarButton("DATE OF ARRIVAL", close_when_date_chosen=True,  target='-ARRIVAL-', location=(0,0), no_titlebar=False )],
          [sg.Text('Choose your destination:',size=(30, 1), font='Lucida',justification='left')],
          # Formatting is weird on Mac - also need to change number of rows based on desired appearance
          [sg.Listbox(values=['Havana', 'Moscow', 'Beijing', 'Tehran', 'Damascus', 'Tripoli', 'Sanaa'], size=(40, 5), select_mode='single', key='-DESTINATION-')],
          [sg.Button('Reserve Ticket'), sg.Button('See Reservations'), sg.Exit()]
]

window = sg.Window('привет Airlines', layout)

def format_input_information(values):
    information = "Flight booked!"
    name = '\nName: ' + values['-NAME-']
    information += name
    passport_number = '\nPassport Number: ' + values['-PASSPORT_NUMBER-']
    information += passport_number
    gender = '\nGender: ' 
    if values['-FEMALE-']: 
        gender += 'Female'
    else: 
        gender += 'Male'
    information += gender
    departure_time = '\nDeparture Time: ' + values['-DEPARTURE-']
    information += departure_time
    arrival_time = '\nArrival Time: ' + values['-ARRIVAL-']
    information += arrival_time
    # Listbox will return an array of 1 element because it's marked as 'single', otherwise it would return a larger array
    destination = '\nDestination: ' + values['-DESTINATION-'][0]
    information += destination
    
    return information
    


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Reserve Ticket':
        sg.popup(format_input_information(values))
window.close()

