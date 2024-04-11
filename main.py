#Import for file that contains filepath
import downloadPathConstant

#import modules
import os #allows to open up file locations in local
import shutil #has functions to move files
from PIL import Image
from PIL.ExifTags import TAGS
import pyheif
from PIL import Image
from pillow_heif import register_heif_opener

#constants
downloadPath = downloadPathConstant.downloadFolder
mediaPath = downloadPathConstant.mediaFolder
loopC = 0


#list of media extensions
videoExtension = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.qt', '.flv']
imageExtension = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.webp', '.heic', '.JPG', '.JPEG', '.PNG', '.GIF', '.BMP', '.TIF', '.TIFF', '.WEBP', '.HEIC']
extensionList = videoExtension + imageExtension 



def getListOfFiles(downloadPath):
	res = [file_path.name for file_path in os.scandir(downloadPath) if os.path.isfile(os.path.join(downloadPath, file_path))]
	listOfMediaFiles = [files for ext in extensionList for files in res if ext in files]
	return listOfMediaFiles

def moveFiles(src,dst,file):
	src = os.path.join(src,file)
	#shutil.move(src,dst)
	#delete copy function after done testing
	shutil.copy2(src,dst)	
	
def getMetaDataImage(downloadPath, file):
	path = os.path.join(downloadPath,file)
	print(path)
	for ext in imageExtension:
		if ext in file:
			if ext == ".HEIC":
				# Open the HEIC photo and extract metadata
				register_heif_opener()
				image = Image.open(path)
				exifdata = image.getexif()
				print(exifdata)
			#	with open(path, 'rb') as f:
    			#		heif_file = pyheif.read(f)
    			#		metadata = heif_file.metadata
			
			#	# Print metadata
			#	print("Metadata:")
			#	print(metadata)	
			else:
				image = Image.open(path)
				exifdata = image.getexif()
				print(exifdata)
	
				for tagid in exifdata:
					tagname = TAGS.get(tagid,tagid)
					value = exifdata.get(tagid)
					print(f"{tagname:25}: {value}")
		


def main():
	loopC = 0
	files = (getListOfFiles(downloadPath))
	for file in files:
		moveFiles(downloadPath,mediaPath,file)
		#IDEA why dont we have a tuple to give type of file and location
		for ext in imageExtension:
			if ext in file:
				loopC = loopC + 1
				print(loopC)
				getMetaDataImage(downloadPath,file)
				
		
		



main()
