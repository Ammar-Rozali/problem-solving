from PIL import Image
import os

input_path = 'images/words'
filename = 'images3.jpg'

file_path = os.path.join(input_path, filename)
print(file_path)
old_im = Image.open(file_path)
old_size = old_im.size

# choose new size
new_size = (850, 150)

new_im = Image.new("RGB", new_size, (255, 255, 255))

if old_size[0] < new_size[0]:
    width = round((new_size[0] - old_size[0]) / 2)
else:
    print('original image more width')
    width = 0

if old_size[1] < new_size[1]:
    height = round((new_size[1] - old_size[1]) / 2)
else:
    print('original image more height')
    height = 0

print('width', width)
print('height', height)

new_im.paste(old_im, (round(width), round(height)))

new_im.save(os.path.join(input_path, 'white_'+filename))