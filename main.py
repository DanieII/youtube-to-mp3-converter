from colorama import Fore
from download import download_func


def main():
    print(f'Press {Fore.GREEN}1{Fore.RESET} to download a single video or {Fore.GREEN}2{Fore.RESET} for a playlist')
    choice = input("1/2 ").upper()
    download_func(choice)


if __name__ == "__main__":
    main()

# For linux the seperator needs to be changed
# Use full paths like C:\Users\Name\Desktop otherwise it won't work properly
