import cv2
import time
from deepface import DeepFace
import os
import numpy as np
def capture_image(TIMER_READY=int(2), TIMER_COUNT=int(3)):

    timer_ready = TIMER_READY
    timer_count = TIMER_COUNT

    cap = cv2.VideoCapture(0)
    while True:
        prev = time.time()

        while timer_ready >= 0:
            ret, img = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, "GET READY FOR IMAGE",
                        (0,100), font,
                        1, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('a', img)
            cv2.waitKey(125)

            cur = time.time()
            if cur-prev >= 1:
            	prev = cur
            	timer_ready = timer_ready-1


        prev = time.time()
        while timer_count >= 0:
        	ret, img = cap.read()

        	font = cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(img, str(timer_count),
        				(200, 250), font,
        				7, (0, 255, 255),
        				4, cv2.LINE_AA)
        	cv2.imshow('a', img)
        	cv2.waitKey(125)

        	# current time
        	cur = time.time()
        	if cur-prev >= 1:
        		prev = cur
        		timer_count = timer_count-1
        #
        ret, img = cap.read()
        img_copy = img.copy()

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_copy, "CLICKED IMAGE",
                    (0, 100), font,
                    1, (0, 255, 255),
                    4, cv2.LINE_AA)
        cv2.imshow('a', img_copy)

        cv2.waitKey(2000)
        # cv2.imwrite('face_database/camera.jpg', img)
        break

    cap.release()
    cv2.destroyAllWindows()

    return img

def get_face(img=None):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
    detected_face = DeepFace.detectFace(img, detector_backend = backends[0])
    return detected_face

img = capture_image(int(2),int(3))
cv2.imwrite('face_curr/camera.jpg', img)
backends = ['opencv', 'ssd', 'mtcnn', 'retinaface']
metrics = ["cosine", "euclidean", "euclidean_l2"]
val = 0
for img in os.listdir('face_database'):
    obj = DeepFace.verify('face_curr/camera.jpg', os.path.join('face_database', img), model_name = "VGG-Face", detector_backend = backends[0], distance_metric = metrics[1])
    if obj['verified']:
        print('match found')
        val = 1
        break
if val == 0:
    print('new patient')
    name = input('Enter your name, underscore bw name and surname: ')
    cv2.imwrite(os.path.join('face_database',name)+'.jpg', img)
os.remove('face_curr/camera.jpg')
