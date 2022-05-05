from os import popen

import pytube

import file_converter
import youtube_downloader


def download_with_options():

    print('''
    What do you want?
    (1) Download YouTube Videos Manually
    (2) Download a YouTube Playlist
    (3) Download YouTube Videos and Convert Into MP3
    ''')

    choice = input("Choice: ")

    if choice == "1" or choice == "2":
        quality = input("Please choose a quality (low, medium, high, very high):")
        quality = 'high'
        if choice == "2":
            link = input("Enter the link to the playlist: ")
            print("Downloading playlist...")
            youtube_downloader.download_playlist(link, quality)
            print("Download finished!")
        if choice == "1":
            links = youtube_downloader.input_links()
            for link in links:
                youtube_downloader.download_video(link, quality)
    elif choice == "3":
        links = youtube_downloader.input_links()
        for link in links:
            print("Downloading...")
            filename = youtube_downloader.download_video(link, 'low')
            print("Converting...")
            file_converter.convert_to_mp3(filename)
    else:
        print("Invalid input! Terminating...")

def download_videos():
    links = youtube_downloader.input_links()
    quality = 'high'
    for link in links:
        path = youtube_downloader.download_video(link, quality)
    print(f'Download finished. path = {path}')
    popen('explorer D:\Eclipse workspace\youtube_downloader')


if __name__ == "__main__":
    download_with_options()
