#Import for file that contains filepath
import downloadPathConstant

#import modules
import os #allows to open up file locations in local
import shutil #has functions to move files

#constants
downloadPath = downloadPathConstant.downloadFolder
mediaPath = downloadPathConstant.mediaFolder

#list of media extensions
videoExtension = [".WEBM",".MPG",".MP2",".MPEG",".MPE",".MPV",".OGG",".MP4",".M4P",".M4V",".AVI",".WMV",".MOV",".QT",".FLV"]
imageExtension = [".apng",".avif",".gif",".jpg",".jpeg",".jfif",".pjpeg",".pjp",".png",".svg",".webp"]


def getListOfFiles(downloadPath):
	res = [file_path.name for file_path in os.scandir(downloadPath) if os.path.isfile(os.path.join(downloadPath, file_path))]
	listOfMediaFiles = [files for ext in imageExtension for files in res if ext in files]
	return listOfMediaFiles

def moveFiles(src,dst,file):
	src = os.path.join(src,file)
	shutil.copy2(src,dst)
	
	


def main():
	files = (getListOfFiles(downloadPath))
	for file in files:
		moveFiles(downloadPath,mediaPath,file)




main()
