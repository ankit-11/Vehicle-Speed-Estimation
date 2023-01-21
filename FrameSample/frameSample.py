import cv2
import argparse
import os

parser = argparse.ArgumentParser(
    description='Frame Sampling for 1 frame per second')
parser.add_argument('-v', type=str)
parser.add_argument('-d', type=str)
args = parser.parse_args()

video = cv2.VideoCapture(args.v)

os.chdir(args.d)
currentframe = 1
fps = int(video.get(cv2.CAP_PROP_FPS))
print('FPS Of Video = ' + str(fps))

# i = 1 for first image
i = 1  # Change value of i as necessary 

while (video.isOpened()):
    ret, frame = video.read()
    if ret:
        if (currentframe % fps == 0):
            # For unique naming, 
            # Use alphabest for user: A for Anish, B for Ankit, P for Pragya
            # Use alphabets for time: M for morning, D for day, E for Evening
            name = 'user' + 'time' + str(i) + '.jpg'
            print('Picture saved :::' + 'user' + 'time' + str(i) + '.jpg')
            cv2.imwrite(name, frame)
            i = i+1
        currentframe += 1
    else:
        break
video.release()
cv2.destroyAllWindows()
