import cv2
image = cv2.imread("abin-pic.jpeg")
cv2.imshow("ABIN", image)
cv2.waitKey(2000)
cv2.destroyAllWindows()