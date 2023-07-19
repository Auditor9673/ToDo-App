from Modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip = "Enter To-Do", key = "todo")

add_button = sg.Button("Add")

window = sg.Window('My To-Do App', 
                   layout=[[label], 
                           [input_box, add_button]], 
                    font = ('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos
            new_todo = values["todo"]
            functions.write_todos(todos)

window.close()