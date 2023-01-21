import cv2
import os
import pathlib
import time
import argparse

parser = argparse.ArgumentParser(description='Crop Before the Crop')
parser.add_argument('-i', type=str)
parser.add_argument('-l', type=str)
parser.add_argument('-d', type=str)
args = parser.parse_args()

Files = os.listdir(args.i)

LFiles = os.listdir(args.l)

for File in Files:
        imgPath = os.path.join(args.i, File)
        print(imgPath)
        img = cv2.imread(imgPath)
        h,w,_ = img.shape
        print(w,h)
        root = pathlib.Path(imgPath).stem
        print(root)

        for LFile in LFiles:
                labelPath = os.path.join(args.l, LFile)
                Lroot = pathlib.Path(labelPath).stem
                if Lroot == root:
                        label = args.l + Lroot + '.txt'
                        print(label)
                        lbl = open(label,'r')
                        i=0
                        while(True):
                                line = lbl.readline()
                                if not line:
                                        break
                                each = line.split()
                                i += 1
                                bBoxCenterX = float(each[1]) * w
                                bBoxCenterY = float(each[2]) * h
                                bBoxWidth = float(each[3]) * w
                                bBoxHeight = float(each[4]) * h
                                 
                                bBoxX1 = int(bBoxCenterX - bBoxWidth/2)
                                bBoxX2 = int(bBoxCenterX + bBoxWidth/2)
                                bBoxY1 = int(bBoxCenterY - bBoxHeight/2)
                                bBoxY2 = int(bBoxCenterY + bBoxHeight/2)
                                
                                print(bBoxX1,bBoxX2,bBoxY1,bBoxY2)
                                
                                crop_img = img[bBoxY1: bBoxY2, bBoxX1: bBoxX2]
                                
                                cropName = args.d + str(root) + '_' + str(i) + '.jpg'
                                cv2.imwrite(cropName,crop_img)
                        lbl.close
                        break;                    
cv2.waitKey(0)

cv2.destroyAllWindows()
