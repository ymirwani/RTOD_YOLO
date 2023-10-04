# $ pip install opencv-python
# $ pip install ultralytics
import cv2
from ultralytics import YOLO

## Webcam input

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img= cap.read()
    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

## Identify the model 

model = YOLO("yolo-Weights/yolov8n.pt")