import cv2
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.nan)

img = cv2.imread("me.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#thresh, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.rectangle(img,(150,50),(330,270),(255,0,255),3)
roi = img[50:270,150:330]
c = 0
color = { 
		0 : 'r+',
		1: 'g+',
		2: 'b+'
		}
# for x in roi:
# 	c +=1
# 	for y in x:

# 		# print roi[c]
# 		plt.plot(c, y,color[c % 3], linewidth = 2.0)

# plt.show()


print np.array(roi)
cv2.imshow("me",img)
cv2.imshow("roi",roi)
cv2.waitKey()
cv2.destroyAllWindows()