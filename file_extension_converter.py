import os


def convert(file):
    root = os.path.splitext(file)[0]
    os.rename(file, root + ".mp3")
