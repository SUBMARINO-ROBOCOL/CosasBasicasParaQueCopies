import cv2
import Codigo_ranas

def crop(frame, dim, is_singular=True):
    if is_singular:
        frame = frame[dim:-dim, dim:-dim]

    Codigo_ranas.main(frame)



