import sys
from pytube import YouTube
from youtubeing import uniquelink

sys.stdout = open(f".\streams.txt", "w", encoding="utf-8")


def print_video_info(video_link):

    try:

        video = YouTube(video_link)

        print(f"\nVideo Title: {video.title}")
        print(f"Video Link: {video_link}")
        # all
        streams = video.streams.all()
        for stream in streams:
            print(stream)

        # progressive
        print("==== Progressive =====")
        streams = video.streams.filter(progressive=True).all()
        for stream in streams:
            print(stream)

        # adaptive
        print("==== Adaptive =====")
        streams = video.streams.filter(adaptive=True).all()
        for stream in streams:
            print(stream)

        # audio
        print("==== Audio =====")
        streams = video.streams.filter(only_audio=True).all()
        for stream in streams:
            print(stream)

        for stream in streams:
            print(stream)
    except:
        pass


for link in uniquelink:
    print_video_info(link)
