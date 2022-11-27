import os
from colorama import Fore


def ask():
    print(f"Choose {Fore.GREEN}Y{Fore.RESET} if you want to create a folder first or {Fore.GREEN}N{Fore.RESET} if you already know where to store the file? ")
    choice = input("Y/N ").upper()
    return choice


def create_folder():
    backslash = "\\"
    directory = input(f"Where do you want the folder to be? Example D:{backslash} ")
    folder_name = input("How do you want the folder to be named? ")
    path = directory + backslash + folder_name
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Folder already exists!!! Try choosing another option.")
        create_func()
    return path


def create_file_only():
    path = input(f"Where do you want the file to be downloaded? Example: D:\songs ")
    return path


def create_func():
    while True:
        choice = ask()
        if choice == "Y":
            final_path = create_folder()
            break
        elif choice == "N":
            final_path = create_file_only()
            break
        else:
            print("Invalid operation. Try again")
            continue
    return final_path
