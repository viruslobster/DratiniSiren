import cv2

pic = cv2.imread('elTesto.png')

pic = 255 - cv2.inRange(pic, (80, 60, 30), (120, 105, 75))

scores = {}

for i in range(1, 152) :
    template = cv2.imread('pokemanz/' + str(i).zfill(3) + '.png', 0)

    res = cv2.matchTemplate(pic, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    scores[str(i).zfill(3)] = max_val

for key, value in sorted(scores.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
