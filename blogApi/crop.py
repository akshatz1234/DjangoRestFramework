from PIL import Image
import numpy as np

im = Image.open('/home/akshatz/Documents/DjangoRestFramework/blogApi/media/IMG_20200702_210159 (2).jpg')

np = np.array(im)
print(np)
# ![lena](data/src/lena.jpg)
print("Done")
im_crop = im.crop((100, 75, 30, 100))
im_crop.save('lena_pillow_crop.jpg', quality=95)

im.crop((100, 75, 300, 150)).save('lena_pillow_crop.jpg', quality=95)

# # ![lena_pillow_crop](data/dst/lena_pillow_crop.jpg)

im_crop_outside = im.crop((100, 175, 300, 250))
im_crop_outside.save('lena_pillow_crop_outside.jpg', quality=95)

