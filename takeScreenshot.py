import cv2

def takeScreenshot():
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("picture1.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

takeScreenshot()