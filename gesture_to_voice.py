
import cv2  
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3

mpHands = mp.solutions.hands

hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)

mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()

print("Hand Gesture Robot")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''
    count = 0
    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        #print(result.multi_hand_landmarks)
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                count += 1

                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                
                landmarks.append([lmx, lmy])
                
            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

            if className == 'one':
                statement = 'one'

            elif className == 'two':
                statement = 'two'

            elif className == 'three':
                statement = 'three'


            elif className == 'four':
                statement = 'four'

                
            elif className == 'super':
                statement = 'i am fine'


            elif className == 'up':
                statement = 'go up'

            elif className == 'down':
                statement = 'go down'

            elif className == 'call':
                statement = 'Call me'


            elif className == 'smile':
                statement = 'smile please'

                
            elif className == 'zero':
                statement = 'stop'

            else:
                statement = ''

            if len(statement.strip()) > 0:
                myobj = gTTS(text=statement, lang='en', slow =False)
                myobj.save("voice.mp3")
                song = MP3("voice.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load('voice.mp3')
                pygame.mixer.music.play()
                time.sleep(song.info.length)
                pygame.quit()
                
            # show the prediction on the frame
            cv2.putText(frame, className, (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0,0,255), 2 )
            
    # Show the final output
    cv2.imshow("Gesture to voice", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
