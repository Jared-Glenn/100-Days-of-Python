from PIL import Image, ImageDraw, ImageFont


class Watermarker:
    def __init__(self):
        self.margin = 10
        self.im = None
        self.width, self.height = None, None
        self.draw = None
        self.text = None
        self.color = None
        self.font = None
        self.textwidth, self.textheight = None, None
        self.x = None
        self.y = None

    def mark_image(self, image, save_name, text, color, x, y, font_size):
        self.im = Image.open(image)
        self.width, self.height = self.im.size
        self.draw = ImageDraw.Draw(self.im)

        self.text = text

        if color == "black":
            self.color = (0, 0, 0)
        elif color == "white":
            self.color = (255, 255, 255)
        else: # Gray
            self.color = (80, 80, 80)

        self.font = ImageFont.truetype('arial.ttf', font_size)
        self.textwidth, self.textheight = self.draw.textsize(text, self.font)

        # x-value
        if x == "left":
            self.x = self.margin
        elif x == "middle":
            self.x = (self.width/2) - (self.textwidth/2)
        else: # Right
            self.x = self.width - self.textwidth - self.margin

        # y-value
        if y == "top":
            self.y = self.margin
        elif y == "middle":
            self.y = (self.height/2) - (self.textheight/2)
        else: # Right
            self.y = self.height - self.textheight - self.margin


        # Draw watermark in the bottom right corner
        self.draw.text((self.x, self.y), self.text, self.color, font=self.font)
        rgb_im = self.im.convert('RGB')

        # Save watermarked image
        rgb_im.save(save_name)
