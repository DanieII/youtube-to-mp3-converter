import pytube
from create_folder import path_func
from file_extension_converter import convert


def download_video(url, path):
    video = pytube.YouTube(url)
    print("Downloaded", video.title)
    result = video.streams.filter(only_audio=True).first().download(path)
    # Turning it into a MP3 file
    convert(result)


def download_func(option):
    while True:
        choice = option
        # Video
        if choice == "1":
            url = input("Enter an url for the video\n")
            path = path_func()
            print(f"Downloading...")
            download_video(url, path)
            break
        # Playlist
        elif choice == "2":
            url = input("Enter the url for the playlist\n")
            path = path_func()
            playlist = pytube.Playlist(url)
            videos = playlist.video_urls
            for video in videos:
                download_video(video, path)
            break
        else:
            print("Try choosing a correct option")
            continue
