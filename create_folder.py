import os


def path_func():
    directory = input(f"Where do you want the folder to be?\n")
    folder_name = input("How do you want it to be named?\n")
    path = directory + "\\" + folder_name
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Folder already exists!!! Terminating...")
        quit()
    return path
