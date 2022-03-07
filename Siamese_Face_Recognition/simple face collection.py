import cv2
import numpy as np
import os

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image

    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(img, 1.3, 5)

    if faces is ():
        return None

    # Crop all faces found
    for (x, y, w, h) in faces:
        x = x - 10
        y = y - 10
        cropped_face = img[y:y + h + 50, x:x + w + 50]

    return cropped_face


# Initialize Webcam
video_capture = cv2.VideoCapture(0)
name = input("Enter name of person:")
path = 'images'
print(path)
directory = os.path.join(path, name)
print(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok='True')
number_of_images = 0
MAX_NUMBER_OF_IMAGES = 10
count = 0
while number_of_images < MAX_NUMBER_OF_IMAGES:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face_extractor(frame), (224, 224))
    if count == 5:
        cv2.imwrite(os.path.join(directory, str(name + str(number_of_images) + '.jpg')), face)
        number_of_images += 1
        count = 0
    print(count)
    count += 1
    cv2.imshow('Video', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
video_capture.release()
cv2.destroyAllWindows()