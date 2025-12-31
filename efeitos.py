from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

img = Image.open("eu.jpg").convert("RGB")

blur = img.filter(ImageFilter.GaussianBlur(5))
img = Image.blend(img, blur, alpha=0.2)
img.show()
img.save("insta_05_glow.jpg")
