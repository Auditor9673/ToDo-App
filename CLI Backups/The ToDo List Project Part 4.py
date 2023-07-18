from Modules import functions


while True:

    action = input("type add, show, edit, complete, or exit: ")


    if action.startswith ('add'):
        todo = action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif action.startswith ('show'):   

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            ind = index + 1
            sho = f"{ind}. {item}"
            print(sho)


    elif action.startswith ('edit'):

        try:
            num = int(action[5:]) -1
            edi = input('enter a new todo: ') + "\n"

            todos = functions.get_todos()
                
            todos[num] = todos[num].replace(todos[num], edi)
            
            functions.write_todos(todos)

        except:
            print("Please enter a valid command!!")
            continue


    elif action.startswith ('complete'):

        try:
            todos = functions.get_todos() 

            dele = int(action[9:]) -1
            rem = todos[dele]
            removed = rem.strip("\n")
            todos.remove(rem)

            functions.write_todos(todos)

            print(f'ToDo "{removed}" was removed from the list.')

        except:
            print("Please enter a valid command!!")
            continue


    elif action.startswith ('exit'):
        exit("bye!")


    else:
        print("Command Not Found!!!")