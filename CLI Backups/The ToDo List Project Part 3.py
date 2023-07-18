while True:
    action = input("type add, show, edit, complete, or exit: ")
    match action:
        case 'add':
            todo = input("enter a todo: ") +"\n" 
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'w') as file:
                file.writelines(todos)
        case 'show':   
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                ind = index + 1
                sho = f"{ind}. {item}"
                print(sho)
        case 'edit':
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                ind = index + 1
                sho = f"{ind}. {item}"
                print(sho)
            number = input("Enter the number of todo to edit from the list of todos above: ")
            num = int(number) -1
            edi = input('enter a new todo: ') + "\n"
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
                todos[num]
                todos[num] = todos[num].replace(todos[num], edi)
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                ind = index + 1
                sho = f"{ind}. {item}"
                print(sho)
            dele = int(input("Selct the number of the completed one from the list of todos above: ")) - 1
            rem = todos[dele]
            todos.remove(rem)
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'w') as file:
                file.writelines(todos)
            print("Now remaining todos are:")
            with open('Z:\Projects\Python files\Text Files For Projects\ToDo.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                ind = index + 1
                sho = f"{ind}. {item}"
                print(sho)
        case 'exit':
            print("bye!")
            exit()