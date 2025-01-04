"""from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('_11_6_cat.JPG')
im_2 = new_photo('_11_6_sun.png')

im.paste(im_2, box = (100, 400))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype(
    font='ofont.ru_Izvod.ttf',
    size=150
)
text = 'С Новым Годом!!'
draw.text(
    text=text,
    font=font,
    xy=(200, 620),
    fill='red'
)

# im.show()
im.show()"""

# ---------------------------------
# Some additional info

from PIL import Image, ImageFont, ImageDraw

class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((
            paste_image.size[0] // 2,
            paste_image.size[1] // 2,
        ))
        self.image.paste(paste_image, box=(200, 200))

    def uprade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(
            font='ofont.ru_Izvod.ttf',
            size=60,
        )
        draw.text(
            xy=(150, 100),
            text=text,
            font=font,
        )

    def show(self):
        self.image.show()


image = PostMaker('_11_6_cat.JPG')
image.paste('_11_6_sun.png')
image.uprade('С Новым Годом!')
image.show()



