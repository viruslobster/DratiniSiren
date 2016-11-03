import sys
import cv2
import numpy
import pygame

DRATINI_THRESH = 85000000.0
username = 'pokebot8311a@gmail.com'
password = 'pokebot8311a!'
emails = []

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'sent email'
    except:
    	print "failed to send mail"


def dratini_bitches():
    for email in emails :
        send_email(username, password, email, '', 'Dratini!!!');
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
