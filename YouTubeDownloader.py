from pytube import YouTube

DW_PATH = input('Path to save the video: ')

url = input('URL video: ')

obj = YouTube(url)

stream = obj.streams.get_highest_resolution()

stream.download(DW_PATH)
