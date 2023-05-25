import cv2
im2=cv2.imread("poster.jpg")
rocket=im2[120:360,400:500]
im2[0:240,500:600]=rocket

texttoshow="rocket into the solar system"
cv2.putText(im2,texttoshow,(20,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,
            color=(0,0,255))
cv2.imshow("poster",im2)
cv2.waitKey(0)
