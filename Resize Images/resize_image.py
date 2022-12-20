# Increase size of images
from PIL import Image

image = Image.open("Image location")

new_image = image.resize((8000, 8000))
new_image.save('Save location')