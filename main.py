import cv2

src=cv2.imread("Basab.jpeg",cv2.IMREAD_UNCHANGED)

cv2.imshow("title",src)
cv2.waitKey(0)

#percent by which the image is resized
scale_percent=50

#calculate 50 percent of original dimensions
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

#resize the image
output=cv2.resize(src,(new_width,new_height))
cv2.imwrite('new_Basab.jpeg',output)
cv2.waitKey(0)