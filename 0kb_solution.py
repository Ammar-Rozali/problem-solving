import cv2

path_0_kb = 'images/words/0kb_image.jpg'
replace_path = 'images/words/blank_image.jpg'

image = cv2.imread(path_0_kb)

if image is not None:
    print('Nothing to change')
else:
    print('will change with blank image')
    replace_path = cv2.imread(replace_path)
    cv2.imwrite(path_0_kb[:-4] + 'replace.jpg', replace_path)
