import cv2

from preprocessing import rgb_to_grayscale
from preprocessing import rgb_to_binary

image = cv2.imread("../dataset/celebrity_faces/mahalini.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = rgb_to_grayscale(image)

binary = rgb_to_binary(image)

cv2.imshow("Gray", gray)
cv2.imshow("Binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()