import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axes

np.set_printoptions(threshold=np.nan)


img = cv2.imread("me.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#thresh, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.rectangle(img,(150,50),(330,270),(255,0,255),3)
imgRoi = img[50:270,150:330]
print imgRoi.shape
#RP = imgRoi.shape[0] / 100 if imgRoi.shape[0] <= imgRoi.shape[1] else imgRoi.shape[1] / 100
#imgRoi = cv2.resize (imgRoi, (imgRoi.shape[1] / RP, imgRoi.shape[0] / RP))

#imgRoi = cv2.resize (imgRoi, (80,80))

###########################################################################################
##cascadefeature1
###########################################################################################
l,w = imgRoi.shape
print l,w

plt.xlabel('X-coordinates')
plt.ylabel('Y-coordinates')
plt.title('Cascade feature 1')
axes.set_xscale(1)
axes.set_yscale(1)
#plt.grid(True)

for i in xrange(w-1):
	for j in xrange(l-1):
		if (imgRoi[j,i]-imgRoi[j,i+1]) >200 or (imgRoi[j,i]-imgRoi[j,i+1]) <-200:
			plt.xlim([0,180])
			plt.ylim([220,0])
			plt.plot(i,j,'b+')
plt.show()	 

###########################################################################################

# c = 0
# color = { 
# 		0 : 'r+',
# 		1: 'g+',
# 		2: 'b+'
# 		}
# for x in roi:
# 	c +=1
# 	for y in x:

# 		# print roi[c]
# 		plt.plot(c, y,color[c % 3], linewidth = 2.0)

# plt.show()


#print imgRoi
#cv2.imshow("me",img)
cv2.imshow("roi",imgRoi)
cv2.waitKey()
cv2.destroyAllWindows()