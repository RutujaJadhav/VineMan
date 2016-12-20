import cv2
import numpy as np
from matplotlib import pyplot as plt





img = cv2.imread('/home/rutuja/CERELABS/DATASET/IMG8.jpg',0)
rgb=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
#img = cv2.GaussianBlur(img,(5,5),0)
edges = cv2.Canny(img,100,200)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(edges,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=35,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    #cv2.circle(edges,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(edges,(i[0],i[1]),2,(0,0,255),3)
 
##plt.subplot(121),plt.imshow(img)
##plt.title('Original Image'), plt.xticks([]), plt.yticks([])
##plt.subplot(122),plt.imshow(edges)
##plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
##
##plt.show()

plt.imshow(rgb)
plt.show()
plt.imshow(edges)
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
