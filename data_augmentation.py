import os
import random
from scipy import ndarray

# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io


def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)


def random_noise(image_array: ndarray):
    # add random noise to the image
    return sk.util.random_noise(image_array)


def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]


# dictionary of the transformations we defined earlier
available_transformations = {
    'rotate': random_rotation,
    'noise': random_noise,
    'horizontal_flip': horizontal_flip
}

folder_path = 'images'

# how many image want to duplicate
num_files_desired = 10

# find all files paths from the folder
folders = ([name for name in os.listdir(folder_path)
            if os.path.isdir(os.path.join(folder_path, name))])

print(folders)

print("Done part 1")

for foldername in folders:
    foldername_path = os.path.join(folder_path, foldername)
    images = os.listdir(os.path.join(folder_path, foldername))
    images = [os.path.join(foldername_path, f) for f in os.listdir(foldername_path) if
              os.path.isfile(os.path.join(foldername_path, f))]

    print(images)
    cnt = len(images)
    total = num_files_desired - cnt
    print(foldername)
    print(cnt)
    print(total)

    num_generated_files = 0
    while num_generated_files < total:
        try:
            # random image from the folder
            image_path = random.choice(images)
            # read image as an two dimensional array of pixels
            image_to_transform = sk.io.imread(image_path)
            # random num of transformation to apply
            num_transformations_to_apply = random.randint(1, len(available_transformations))
            print("done part 2")

            num_transformations = 0
            transformed_image = None
            while num_transformations <= num_transformations_to_apply:
                # random transformation to apply for a single image
                key = random.choice(list(available_transformations))
                transformed_image = available_transformations[key](image_to_transform)
                num_transformations += 1

            print("done part 3")

            new_file_path = '%s/augmented_image_%s.jpg' % (foldername_path, num_generated_files)

            # write image to the disk
            io.imsave(new_file_path, transformed_image)
            num_generated_files += 1

            print("done part 4")
        except Exception as e:
            print('Error', e)
            print('iamge cannot duplicate', image_path)
