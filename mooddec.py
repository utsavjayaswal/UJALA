# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:52:59 2020

@author: utsav
"""


def mooddetect():
    import numpy as np
    import cv2
    from keras.preprocessing import image
    
    face_cascade = cv2.CascadeClassifier('C:/Users/utsav/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    #cap = cv2.VideoCapture(0)
    #cap=cv2.imread('maintest.jpeg')
    from keras.models import model_from_json
    model = model_from_json(open("facial_expression_model_structure.json", "r").read())
    model.load_weights('facial_expression_model_weights.h5') #load weights
    
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    temp=[]
    #for i in range(50):
        
    #ret, img = cap.read()
    img=cv2.imread('maintest.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image
        detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
        detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
        detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48
            
        img_pixels = image.img_to_array(detected_face)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
            
        img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]
        predictions = model.predict(img_pixels)
            
        max_index = np.argmax(predictions[0])
            
        emotion = emotions[max_index]
            
            
        cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        
        temp.append(emotion)
            
    cv2.imshow('img',img)
    cv2.waitKey(10000)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
    #cap.release()
    cv2.destroyAllWindows()
    
    
    return temp

aj=mooddetect()
print(aj)


            
            