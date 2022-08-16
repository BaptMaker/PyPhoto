from PIL import Image
from PIL.ExifTags import TAGS
from os import walk
import os, shutil
  
def metadata(img: str):
    """Argument: name of the image\nReturn: A dictionary with the metadata"""
    # open the image
    image = Image.open(img)
  
    # extracting the exif metadata
    exifdata = image.getexif()
    
    # create a list of the metadata
    metaData = {}

    # looping through all the tags present in exifdata
    for tagid in exifdata:
      
        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)
  
        # passing the tagid to get its respective value
        value = exifdata.get(tagid)
    
        # printing the final result
        metaData[tagname] = value
    return metaData

def nameFile(directory: str):
    # The liste of file
    listeFichiers = []
    # search the file
    for (repertoire, sousRepertoires, fichiers) in walk(directory):
        # Add file to the list
        listeFichiers.extend(fichiers)
        break
    result = []
    for files in listeFichiers:
        extention = files.split(".")
        if extention[1] == "jpg" or extention[1] == "JPG" or extention[1] == "png" or extention[1] == "jpeg":
            result.append(files)
    return result

def tri(meta: dict, name: str):
    try:
        fileTime = meta["DateTime"].split(" ")
        if not os.path.exists(fileTime[0]):
            os.makedirs(fileTime[0])
        shutil.move(name, f"{fileTime[0]}/{name}")
    except:
        print(f"Le fichier <{name}> n'a pas pu ètre trier.")

if __name__ == "__main__":
    N = nameFile("./")
    for test in N:
        m = metadata(test)
        tri(meta=m,name=test)