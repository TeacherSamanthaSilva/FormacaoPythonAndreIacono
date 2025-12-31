from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

img = Image.open("eu.jpg").convert("RGB")

img_nitidez = ImageEnhance.Sharpness(img).enhance(1.5)
img_nitidez.save("05_nitidez.jpg")
img_nitidez.show()

