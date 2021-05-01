import cv2
import os
import sys
from pathlib import Path

targetDir = sys.argv[1]

def bitify(f,fp,np):

    input = cv2.imread(fp)
    theight, twidth = input.shape[:2]
    if theight <= 512 and twidth <= 512:
        timg = cv2.resize(input, (64, 64), interpolation=cv2.INTER_LINEAR)
    else:
        timg = cv2.resize(input, (256, 256), interpolation=cv2.INTER_LINEAR)
    newimg = cv2.resize(timg, (twidth, theight), interpolation=cv2.INTER_NEAREST)
    outputFile = np + os.sep + f
    cv2.imwrite(outputFile,newimg)

for subdir, dirs, files in os.walk(targetDir):
    for file in files:
        filepath = subdir + os.sep + file
        os.chdir(targetDir)
        os.chdir("..")
        newfolder = Path.cwd()
        newpath = os.path.join(newfolder,"Output") 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        bitify(file, filepath, newpath)


