from pytube import YouTube


video = YouTube('https://www.youtube.com/watch?v=syGeHKMlz98')
streams = video.streams.all()

print(streams[0])
print(streams[0].itag)


# Lists of stream properties
quality = [stream.mime_type for stream in streams]
itag = [stream.itag for stream in streams]
res = [stream.resolution for stream in streams]

print(f"Quality - {quality}\n")
print(f"Itag - {itag}\n")

# Dictionary quality:itag
quality_itag = {stream.resolution: stream.itag for stream in streams}
itag_quality = {stream.itag: stream.resolution for stream in streams}

print(f"Dictionary: {quality_itag}")
print(f"Dictionary: {itag_quality}")
