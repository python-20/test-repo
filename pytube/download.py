from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
streams = yt.streams.all()

for stream in streams:
    if stream.mime_type == "video/mp4" and stream.resolution != None:
        print(stream)

#adaptive_test_file = yt.streams.get_by_itag('137')

# stream.download(".\downloads")
