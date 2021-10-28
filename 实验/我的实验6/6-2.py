from PIL import Image
from PIL import ImageFilter
im = Image.open('first.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('second.jpg')
