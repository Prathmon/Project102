import cv2
import dropbox
import time
import random

start_time = time.time()

def takeSnapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("Snapshot taken.")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(image_name):
    access_token = ""
    file = image_name
    file_from = file
    file_to = "/testfolder/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    with_open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_2, mode=dropbox.files.writemode.overwrite).read()

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = takeSnapshot()
            upload_file(name)

main()