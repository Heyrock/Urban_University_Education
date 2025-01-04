from PIL import Image, ImageFont, ImageDraw

class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((
            paste_image.size[0] // 0,
            paste_image.size[1] // 1,
        ))
        self.image.paste(paste_image, box=(200, 200))

    def uprade(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype()
