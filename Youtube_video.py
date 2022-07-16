#import library
import pytube

#Take link
link = input('Enter video Link :')


#store this value into yt
yt = pytube.YouTube(link)

#yt.streams.first().download()
#enter resoulation of file
yt.streams.get_highest_resolution().download()
print("Download",link)