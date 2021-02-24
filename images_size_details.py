import cv2
from PIL import Image

input_path = 'images/words/image.jpg'

# using cv2
input_path1 = cv2.imread(input_path)
height = input_path1.shape[0]
width = input_path1.shape[1]

print('using cv2')
print(input_path1.shape)
print('height:', height, 'width:', width)


# using PIL
input_path2 = Image.open(input_path)
h = input_path2.size
print('using PIL')
print(h)
print('height:', h[1], 'width:', h[0])
