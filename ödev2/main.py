import cv2
import numpy as np
vid = cv2.VideoCapture(0)

while (True):
    ret, frame = vid.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red_1 = np.array([0, 61, 38]) #Maske için alt aralık
    upper_red_1 = np.array([9, 255, 255]) #Maske için üst aralık


    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1) #Maske oluşturma

    result = cv2.bitwise_and(frame, frame, mask=mask1) #Maskeyi iliştirme


    cv2.imshow('Result', result)
    cv2.imshow('Mask', mask1)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()