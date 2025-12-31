from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

img = Image.open("eu.jpg").convert("RGB")

img_cor = ImageEnhance.Color(img).enhance(1.4)
img_cor.save("03_saturacao.jpg")
img_cor.show()
