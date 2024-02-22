import cv2                          # pip install opencv-python

array = cv2.imread("image.png")

print(array.shape)         # BGR -->>> openCV work with: Blue, Green, Red

print(type(array))
print(array)