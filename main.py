import os
from shutil import copy
import plistlib
from PIL import Image
from sys import platform, argv

path = ""

if platform == "win32":
    path = "C://Program Files (x86)//Steam//steamapps//common//Geometry Dash"
elif platform == "linux" or platform == "linux2":
    path = "~/.local/share/Steam/steamapps/common/Geometry Dash"
elif platform == "darwin":
    path = "~/Library/Application Support/Steam/steamapps/common/Geometry Dash"

if len(argv) >= 2 and type(argv[1]) == str:
    path = argv[1]
elif len(argv) >= 2 and not type(argv[1]) == str:
    print("The first parameter of the script is wrong.")

print("Using game directory: " + path)

if not os.path.exists(os.getcwd() + "//extracted"):
    os.mkdir(os.getcwd() + "//extracted")
for x in os.listdir(path + "//Resources"):
    if x.endswith(".png"):
        plistFile = x.replace(".png", ".plist")
        plistFilePath = path + "//Resources" + "//" + plistFile
        if os.path.exists(plistFilePath):
            print(x)
            img = Image.open(path + "//Resources" + "//" + x)
            file = open(plistFilePath, "rb")
            pl = plistlib.load(file, fmt=plistlib.FMT_XML)
            file.close()
            originalFileName = ""
            currentFileName = ""
            thing = pl["frames"]
            for i in range(len(thing.keys())):
                position = [0, 0]
                size = [0, 0]
                isRotated = False
                originalFileName = list(thing.keys())[i]

                if x.endswith("-hd.png"):
                    currentFileName = list(thing.keys())[i].removesuffix(".png") + "-hd.png"
                elif x.endswith("-uhd.png"):
                    currentFileName = list(thing.keys())[i].removesuffix(".png") + "-uhd.png"
                else:
                    currentFileName = list(thing.keys())[i]

                print("-> " + currentFileName)

                if "textureRect" in thing[originalFileName]:
                    numbers = []
                    string = ""
                    for c in thing[originalFileName]["textureRect"]:
                        if c.isdigit():
                            string += c
                        else:
                            if not string == "":
                                numbers.append(int(string))
                            string = ""
                    position[0] = numbers[0]
                    position[1] = numbers[1]
                    size[0] = numbers[2]
                    size[1] = numbers[3]

                elif "frame" in thing[originalFileName]:
                    numbers = []
                    string = ""
                    for c in thing[originalFileName]["frame"]:
                        if c.isdigit():
                            string += c
                        else:
                            if not string == "":
                                numbers.append(int(string))
                            string = ""
                    position[0] = numbers[0]
                    position[1] = numbers[1]
                    size[0] = numbers[2]
                    size[1] = numbers[3]

                if "textureRotated" in thing[originalFileName]:
                    isRotated = thing[originalFileName]["textureRotated"]
                elif "rotated" in thing[originalFileName]:
                    isRotated = thing[originalFileName]["rotated"]

                print("--> Position: " + str(position))
                print("--> Size: " + str(size))
                print("--> Is Rotated: " + str(isRotated))

                finalImage : Image

                if isRotated:
                    croppedImage = img.crop((position[0], position[1], position[0] + size[1], position[1] + size[0]))
                    finalImage = croppedImage.rotate(90, Image.NEAREST, True)
                else:
                    finalImage = img.crop((position[0], position[1], position[0] + size[0], position[1] + size[1]))

                if os.path.exists(os.getcwd() + "//extracted"):
                    finalImage.save(os.getcwd() + "//extracted//" + currentFileName)
                else:
                    print("The output extracted sprites folder couldn't be found. Aborting...")
                    exit(-1)

        else:
            print(x)
            if os.path.exists(os.getcwd() + "//extracted"):
                copy(path + "//Resources" + "//" + x, os.getcwd() + "//extracted")
            else:
                print("The output extracted sprites folder couldn't be found. Aborting...")
                exit(-1)