import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('/home/rutuja/CERELABS/DATASET/IMG8.jpg')
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lower_green=np.array([110,0,0])
upper_green=np.array([400,400,400])

mask=cv2.inRange(rgb,lower_green,upper_green)
result=cv2.bitwise_and(img,img,mask=mask)
kernel = np.ones((15,15),np.float32)/225
#smoothed = cv2.filter2D(result,-1,kernel)
#blur=cv2.GaussianBlur(result,(15,15),0)
#median=cv2.medianBlur(result,5)
opening=cv2.morphologyEx(result,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel)
erosion=cv2.erode(result,kernel,iterations=1)
dilation=cv2.dilate(result,kernel,iterations=1)



plt.imshow(img)
plt.show()
plt.imshow(result)
plt.show()
plt.imshow(dilation)
plt.show()
plt.imshow(opening)
plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()

