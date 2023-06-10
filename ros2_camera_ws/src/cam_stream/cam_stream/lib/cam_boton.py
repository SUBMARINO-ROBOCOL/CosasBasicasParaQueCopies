import cv2
from PIL import Image
import numpy as np


def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit


def red_box(img):
	bbox = (0,0,0,0)

	color = [0,255,255]
	
	hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
	lowerLimit, upperLimit = get_limits(color)
		
	mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
		
	mask_ = Image.fromarray(mask)
	bbox = mask_.getbbox()
	if bbox is not None:
		x1, y1, x2, y2 = bbox
		img = cv2.rectangle(img, (x1,y1), (x2,y2), (50,50,250), 5)
	
	while True:
		cv2.imshow ("frame", img)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
