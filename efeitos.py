from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

img = Image.open("eu.jpg").convert("RGB")

img_contraste = ImageEnhance.Contrast(img).enhance(1.3)
img_contraste.save("02_contraste.jpg")
img_contraste.show()
