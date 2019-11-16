#video capturing the on screen on desktop
import numpy as np
from PIL import ImageGrab
import cv2
import time



def process_img (org_img):
    processed_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, 200,300)
    return processed_img
last_time = time.time()

while(True):
    printscreen_pil = ImageGrab.grab(bbox = (0,40,800,640))
    #convert to numpy array
    printscreen_pil = np.array(printscreen_pil)
    
    #process the image
    processed_img = process_img(printscreen_pil)
    print('Loop took {} seconds'.format(time.time()-last_time))
    
    last_time  =  time.time()
    cv2.imshow('window',processed_img)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
