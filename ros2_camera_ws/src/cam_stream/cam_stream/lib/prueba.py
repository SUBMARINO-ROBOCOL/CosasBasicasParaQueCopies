import Codigo_ranas
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    Codigo_ranas.main(frame)