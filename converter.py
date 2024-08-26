from imports.libs import convert
import FreeSimpleGUI as sg
import os

# Flag to control the event loop
running = True

# Get the current working directory
working_directory = os.getcwd()

# Define the layout of the GUI
layout = [
    [sg.Text("Converter", font=("Helvetica", 12, "bold"))],
    [sg.Text("File selection window:"), sg.Input(size=(25, 1), key="FILE_PATH"), sg.FileBrowse("Photo Selection", key="BROWSE", file_types=(('PNG', '*.png'), ('JPEG', '*.jpg')), initial_folder=working_directory)],
    [sg.Text("New width (px):"), sg.Slider((0, 1000), orientation='horizontal', key='NEW_WIDTH')],
    [sg.Text("Name of new file:"), sg.Input(size=(25, 1), key="NEW_FILE_NAME"), sg.Button("Auto-create from Path")],
    [sg.Button("Convert")]
]

# Create the window
window = sg.Window('Pixelart converter', layout)

# Event loop
while running:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:  # If the user closes the window
        running = False
    elif event == "Auto-create from Path":
        file_path = values.get('FILE_PATH') 
        if file_path:
            file_name = file_path.split("/")
            file_name = file_name[len(file_name) - 1].split(".")[0]
            window['NEW_FILE_NAME'].update(file_name + "_px")
    elif event == "Convert":  # If the user clicks the "Convert" button
        file_path = values.get('FILE_PATH')  # Retrieve the file path
        new_width = values.get('NEW_WIDTH')  # Retrieve the percentage value
        new_file_name = values.get('NEW_FILE_NAME')
        if file_path:
            file_name = file_path.split("/")
            file_name = file_name[len(file_name) - 1].split(".")[0]
            extension = file_name = file_name[len(file_name) - 1].split(".")[1]
            
            print(f"File selected: {file_path}")
            print(f"Resize width: {new_width}px")
            print(f"File name: {file_name}.{extension}")
            print(f"New File Name: {new_file_name}.{extension}")
            
            convert(file_path, new_width, file_name, new_file_name)
            
# Close the window
window.close()
