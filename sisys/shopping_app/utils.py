from PIL import Image


def resize_image(original_image):
    image = Image.open(original_image)
    img = image.resize((306, 259), Image.ANTIALIAS)
    return img
