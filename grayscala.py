import cv2
import os

path_input = 'images/words'

path = os.listdir(path_input)
print(path)

for filename in path:

    if filename.endswith('.jpg'):
        file_path = os.path.join(path_input, filename)
        image_read = cv2.imread(file_path)

        # grayscala
        gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

        # Another way
        # (thresh, blackAndWhiteImage) = cv2.threshold(image_read, 155, 255, cv2.THRESH_BINARY)

        file_path = file_path[:-4] + '_output.jpg'
        print(file_path)

        cv2.imshow('Original image', image_read)
        cv2.imshow('Gray image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imwrite(file_path, gray)
