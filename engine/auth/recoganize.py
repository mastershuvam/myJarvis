from sys import flags
import time
import cv2
import pyautogui as p

def AuthenticateFace():
    flag = ""
    # Local Binary Patterns Histograms
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('engine/auth/trainer/trainer.yml')  # load trained model
    cascadePath = "engine/auth/haarcascade_frontalface_default.xml"
    # initializing haar cascade for object detection approach
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 2  # number of persons you want to Recognize

    names = ['None', 'Person1', 'Person2']  # names, leave first empty for unknown

    cam = cv2.VideoCapture(0)  # cv2.VideoCapture(0) for web camera
    cam.set(3, 640)  # set video frame width
    cam.set(4, 480)  # set video frame height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()  # read the frames using the above created object
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(converted_image[y:y + h, x:x + w])

            # Check if confidence is less than 100 ==> "0" is perfect match
            if confidence < 100:
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                flag = 1
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                flag = 0

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    return flag