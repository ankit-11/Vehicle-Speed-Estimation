import cv2
video = cv2.VideoCapture('test.mp4')
currentframe=1
fps = int(video.get(cv2.CAP_PROP_FPS))
print('FPS Of Video = ' + str(fps))

while(video.isOpened()):
    ret,frame = video.read() 
    if ret:
        if(currentframe%fps==0):
            name = './frame/' + str(int(currentframe/fps)) + '.jpg'
            print('Picture saved :::'+ str(int(currentframe/fps)) + '.jpg')
            cv2.imwrite(name, frame) 
        currentframe += 1
    else: 
        break
video.release() 
cv2.destroyAllWindows()