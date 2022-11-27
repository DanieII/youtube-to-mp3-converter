import os
from pytube import YouTube
from create_file import create_func
import emoji
from colorama import Fore


def main():
    url = input("Please input an url for the video: ")
    video = YouTube(url)
    # Deciding where to store the file
    path = create_func()

    print(f"Downloading Video!\n{video.title}")
    print(f'{Fore.LIGHTYELLOW_EX}This may take a while{Fore.RESET} {emoji.emojize(":upside-down_face:")}')
    result = video.streams.filter(only_audio=True).first().download(f"{path}")
    new = os.path.splitext(result)
    os.rename(result, new[0] + ".mp3")
    print("Done")


if __name__ == "__main__":
    main()
# TEST INPUTS
# https://www.youtube.com/watch?v=M-mtdN6R3bQ
# C:\Users\User\Desktop
