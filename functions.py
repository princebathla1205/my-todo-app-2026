def get_todos(filepath="todos.txt"):
    """ Read a text file and get the list
    of to-do items """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do into a text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello!")