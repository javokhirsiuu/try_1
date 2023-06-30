from pytube import YouTube

link = input("Enter the silka")

yt = YouTube(link)


print(f"zagolovok:{yt.title}")
print(f"prosmotor:{yt.views}")
print(f"prodoljitelnost video:{yt.length}")

ys = yt.streams.get_highest_resolution()
ys.download()


print("siu")
print("done")


from pytube import YouTube

link = input("Enter the silka2")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
stream.download()

print("done")


