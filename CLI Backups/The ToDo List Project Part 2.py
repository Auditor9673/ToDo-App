todos = []
while True:
    action = input("type add, show, or exit: ")
    match action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show':   
            for item in todos:
                print(item)
        case 'exit':
            print("bye!")
            exit()