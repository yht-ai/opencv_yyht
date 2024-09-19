import cv2
# logo = cv2.imread('F:\\YHT CV\\O1\\3_1.jpg')
# print(logo[190,168])
logo = cv2.imread('./3_1.jpg')
blue = logo[190,168,0]
green = logo[190,168,1]
red = logo[190,168,2]
print(blue,green,red)
print(type(blue))