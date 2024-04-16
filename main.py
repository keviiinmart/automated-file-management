#Import for file that contains filepath
import downloadPathConstant

#import modules
import os #allows to open up file locations in local
import shutil #has functions to move files

#constants
downloadPath = downloadPathConstant.downloadFolder
mediaPath = downloadPathConstant.mediaFolder

#list of media extensions
videoExtension = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.qt', '.flv', '.WEBM', '.MPG', '.MP2', '.MPEG', '.MPE', '.MPV', '.OGG', '.MP4', '.M4P', '.M4V', '.AVI', '.WMV', '.MOV', '.QT', '.FLV']
imageExtension = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.webp', '.heic', '.JPG', '.JPEG', '.PNG', '.GIF', '.BMP', '.TIF', '.TIFF', '.WEBP', '.HEIC']
extensionList = videoExtension + imageExtension 

#check if the download folder has media to move
def checkDownloadFolder():
	path = os.listdir(downloadPath)
	#if len(path) != 0:
	#I personally have ds_store and localized files in my downloads folder
	#if this does now work try zero
	if len(path) != 2:
		return True
	else:
		return False	
	
def getListOfFiles(downloadPath):
	res = [file_path.name for file_path in os.scandir(downloadPath) if os.path.isfile(os.path.join(downloadPath, file_path))]
	listOfMediaFiles = [(files,ext) for ext in extensionList for files in res if ext in files]
	return listOfMediaFiles

def moveFiles(src,dst,file):
	src = os.path.join(src,file)
	try:	
		shutil.move(src,dst)
		#delete copy function after done testing
		#shutil.copy2(src,dst)	
	except:
		pass

def createDirectory(src,directoryName):
	path = os.path.join(src,directoryName)
	os.mkdir(path)
	

def checkIfFolderExist(src,directoryName):
	path = os.path.join(src,directoryName)
	if not os.path.exists(path):
		createDirectory(src,directoryName)
		return path
	else:
		return path

def main():
	if checkDownloadFolder():
		tupleFilesExt = (getListOfFiles(downloadPath))	
		for tuple in tupleFilesExt:
			file = tuple[0]
			ext = tuple[1]
			if ext in imageExtension:
				path = checkIfFolderExist(mediaPath,"pictures")
				moveFiles(downloadPath,path,file)
			elif ext in videoExtension:
				path = checkIfFolderExist(mediaPath,"videos")
				moveFiles(downloadPath,path,file)
	else:
		print("Download folder is empty")



main()
