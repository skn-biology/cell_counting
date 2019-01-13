import cv2


def binarise_image(image, threshold):
    image = image.copy()
    image[image >= threshold] = 255
    image[image < threshold] = 0
    return image

def open_image(file_name):
    image = cv2.imread(file_name)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def save_binarised_image(file_name, threshold):
    image = open_image(file_name)
    binarised_image = binarise_image(image, threshold)
    file_name_binarised = file_name[:-3] + "binerased.TIF"
    return cv2.imwrite(file_name_binarised, binarised_image)


