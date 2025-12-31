from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

img = Image.open("eu.jpg").convert("RGB")

img_brilho = ImageEnhance.Brightness(img).enhance(1.1)
img_brilho.save("04_brilho.jpg")
img_brilho.show()
