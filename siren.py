import sys
import cv2
import numpy
import pygame

DRATINI_THRESH = 28500000.0

def dratini_bitches():
    pygame.mixer.init()
    pygame.mixer.music.load("siren.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

stdin = sys.stdin.read()
array = numpy.frombuffer(stdin, dtype='uint8')
img = cv2.imdecode(array, 0)

template = cv2.imread('dratini.png', 0)

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print max_val

if max_val >= DRATINI_THRESH:
    dratini_bitches()
    exit(0)
else:
    exit(1)
