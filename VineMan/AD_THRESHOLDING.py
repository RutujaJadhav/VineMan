import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/rutuja/CERELABS/DATASET/IMG8.jpg',0)

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.float32)/25
#blur = cv2.filter2D(img,-1,kernel)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in xrange(3):
    plt.subplot(3,3,i*3+
                1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

circles = cv2.HoughCircles(th3,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    #cv2.circle(th3,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    cv2.circle(th3,(i[0],i[1]),2,(0,0,255),3)

#print i
#plt.imshow(th3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

