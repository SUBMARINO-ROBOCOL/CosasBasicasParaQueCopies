import cv2

def main():
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

def returnCameraIndexes():
        index = 0
        arr = []
        while index < 10:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
        if (len(arr)>0):
            print("The following camera indexes were detected: ")
            msg = ""
            for i in arr:
                msg += str(i)+", "
            print(msg[:-2])
        else:
             print("No cameras available \n Please ctrl+c to end task")


print(returnCameraIndexes())