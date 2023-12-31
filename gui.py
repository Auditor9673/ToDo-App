from Modules import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('ToDo.txt'):
    with open('ToDo.txt', 'w') as file:
        pass

sg.theme("DarkTeal10")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip = "Enter To-Do", key = "todo", size=46)

add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key= "todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button],
                           [list_box, edit_button, 
                            complete_button], [exit_button]], 
                    font = ('Helvetica', 14))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%dth %b %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            add_todo = values["todo"] + "\n"
            todos.append(add_todo)
            functions.write_todos(todos)
            window["todos"].update(values= todos)
        
        case sg.WIN_CLOSED:
            break

        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values= todos)
            except IndexError:
                sg.popup('Please select an item first!!', font=('Helvetica', 13))

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window["todos"].update(values= todos)
                window['todo'].update(value = "")
            except IndexError:
                sg.popup('Please select an item first!!')
        
        case "Exit":
            break

window.close()