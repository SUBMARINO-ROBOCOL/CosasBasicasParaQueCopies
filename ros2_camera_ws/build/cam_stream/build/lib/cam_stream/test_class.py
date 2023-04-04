import cv2

cam = cv2.VideoCapture(0)
check = True

while check:
    check, frame = cam.read()

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)

    if key == 113:
        break

cam.release()
cv2.destroyAllWindows()