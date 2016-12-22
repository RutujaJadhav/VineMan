import cv2
import numpy as np
import matplotlib.pyplot as plt
c=0
img = cv2.imread('/home/rutuja/CERELABS/DATASET/IMG8.jpg',0)
rgb=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

#t_o = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cimg = cv2.cvtColor(img,cv2.COLOR_bgr2BGR)


circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=35,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    c=c+1
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    a=cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    
print "approx count is "+str(c)
plt.imshow(rgb)
plt.show()
plt.imshow(img)
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()

