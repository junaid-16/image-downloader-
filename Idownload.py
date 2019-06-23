#python3 program to download the images from internet
#it uses google_images_download python library to download the image
from google_images_download import google_images_download

#creating object
download = google_images_download.googleimagesdownload()

#downloading functions
def downloadimages():
	keyword=input("enter the keyword to search: ")
	limit=int(input("enter the no. of images you want to download: "))
    
    #varialbe 'argument' will be used to pass the argument to download function
	arguments={"keywords": keyword, "limit":limit}

	download.download(arguments)
#calling the function
downloadimages()