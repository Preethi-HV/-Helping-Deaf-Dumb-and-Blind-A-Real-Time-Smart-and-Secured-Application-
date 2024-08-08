# Import required packages
import cv2
import pytesseract
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# Read image from which text needs to be extracted
img = cv2.imread("C:\\Users\\Preethi Aradhya\\Desktop\\deaf_dumb_blind\\deaf_dumb_blind\\image1.jpg")


# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()
        
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
text1=''
for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        text1 += ''+pytesseract.image_to_string(cropped)

print('\n--------------Recognized Text------------\n')
print(text1)  
myobj = gTTS(text=text1, lang='en', slow =False)
myobj.save("voice.mp3")
print('\n--------------Playing------------\n')
song = MP3("voice.mp3")
pygame.mixer.init()
pygame.mixer.music.load('voice.mp3')
pygame.mixer.music.play()
time.sleep(song.info.length)
pygame.quit()

cv2.imshow('Image to voice', im2)
