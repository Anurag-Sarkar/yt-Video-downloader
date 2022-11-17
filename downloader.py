from pytube import YouTube
from pytube import Playlist

l = input("enter link: ")
try:
    link = YouTube(l)
except Exception as e:
    print("Invalid Link!!!!")
    exit()
print("1. Only Audio")
print("2. Only Video")
print("3. Playlist")
choice = int(input("Enter Choice: "))
if choice == 1:
    availabe = link.streams.filter(only_audio=True)
    for i,v in enumerate(availabe):
        vi = str(v)
        vi = vi.split(" ")[3]
        print(f"{i+1}. {vi[5:-1]}")
    option = int(input("enter option: "))
    if option-1 < len(availabe):
        itag = str(availabe[option-1]).split(" ")
        itag = itag[1]
        itag = itag[6:-1]
        itag = int(itag)
        link.streams.get_by_itag(itag).download("./audio")
        print("Downloading...",link.title)

elif choice == 2:
    availabe = link.streams.filter(progressive=True,file_extension="mp4")
    for i,v in enumerate(availabe):
        vi = str(v)
        vi = vi.split(" ")[3]
        print(f"{i+1}. {vi[5:-1]}")

    option = int(input("enter option: "))
    if option-1 < len(availabe):
        itag = str(availabe[option-1]).split(" ")
        itag = itag[1]
        itag = itag[6:-1]
        itag = int(itag)
        link.streams.get_by_itag(itag).download("./videos")
        print("Downloading...", link.title)
elif choice == 3:
    p = Playlist(l) 

    option = input("Audio or Video: ")
    if option.lower() == "audio":
        try:
            for i in p.videos:
                print("Downloading",i.title)
                i.streams.get_audio_only().download("./audio")
        except Exception:
            print("link isnt a playlist!!!")

    elif option.lower() == "video":
        try:
            for i in p.videos:
                print("Downloading",i.title)
                i.streams.get_highest_resolution().download("./video")
        except Exception:
            print("link isnt a playlist!!!")
        