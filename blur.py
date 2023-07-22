from PIL import Image,ImageFilter
before = Image.open("input.jpeg")
portrait_or_squared = before.width<before.height or before.width==before.height
after = before.filter(ImageFilter.BoxBlur(10))
if portrait_or_squared:
    after = after.rotate(-90, expand=True)
after.save("blurred.bmp")
