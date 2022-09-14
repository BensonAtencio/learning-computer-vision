import cv2

img = cv2.imread('C:\\Users\\MARASIGAN\\repository\\learning-computer-vision\\random\\assets\\Facebook-logo.png', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imwrite('new-fb-logo.png', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
