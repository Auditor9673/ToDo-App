import time
now = time.strftime("%dth %b %Y, %H:%M:%S")
print("It is", now)


def get_todos(filepath = 'The ToDo List Project\Text Files\ToDo.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = 'The ToDo List Project\Text Files\ToDo.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)