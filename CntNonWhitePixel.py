import cv2
import os

count = 0
path = 'images/words'
listing = []
length = []
count_l= 0
for list in os.listdir(path):
    if list.endswith('.jpg'):
        print(list)

        img_path = os.path.join(path, list)

        image = cv2.imread(img_path, 0)

        _, img = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)

        # get all non black Pixels
        cntWhitePixel = cv2.countNonZero(img)
        # get pixel count of image
        height, width = img.shape
        cntPixels = height*width

        # compute all black pixels
        cntNonWhite = cntPixels - cntWhitePixel
        print('cntPixels', cntPixels)
        print('cntWhitePixel', cntWhitePixel)
        print('cntNonWhite', cntNonWhite)

        percentage = (cntNonWhite/cntPixels)*100
        print(f'cntNonWhite pixel percentage {percentage:.2f}')

