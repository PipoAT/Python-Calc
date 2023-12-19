import PySimpleGUI as sg

# define the layout of the GUI
layout = [
    [sg.Text("Enter First Number:")],
    [sg.Input()],
    [sg.Button("+", key="+"), sg.Button("-", key="-"), sg.Button("*", key="*"), sg.Button("/", key="/")],
    [sg.Text("Enter Second Number:")],
    [sg.Input()],
    [sg.Button("Calculate"), sg.Button("Exit")]
]

# create the window
window = sg.Window("Python Calculator", layout)

while True:
    # interact with window
    event, values = window.read()

    # if user closes window or clicks exit
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event in ["+", "-", "*", "/"]:
        operation = event
        window[event].update(button_color=('white', 'green'))
        # Set the other buttons to dark blue
        for op in ["+", "-", "*", "/"]:
            if op != event:
                window[op].update(button_color=('white', 'dark blue'))

    if event == "Calculate":
        first_value = float(values[0])
        second_value = float(values[1])
        if operation == "+":
            result = first_value + second_value
        elif operation == "-":
            result = first_value - second_value
        elif operation == "*":
            result = first_value * second_value
        elif operation == "/":
            result = first_value / second_value

        sg.popup(result)
        # Reset the color of operation buttons after calculation
        for op in ["+", "-", "*", "/"]:
            window[op].update(button_color=('white', 'dark blue'))

# close window
window.close()
