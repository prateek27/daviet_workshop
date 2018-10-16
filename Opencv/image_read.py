import cv2

image = cv2.imread("dog.png")
#print(image.shape)

cv2.imshow("My Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()



