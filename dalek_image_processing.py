from PIL import Image, ImageFilter



def dalekview(img):


    img1 = img.split()

    out = img1[2].point(lambda i: i * 1.5)

    img1[2].paste(out, None, None)

    return Image.merge(img.mode, img1)