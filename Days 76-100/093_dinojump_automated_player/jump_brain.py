import pyautogui
import mss
from PIL import Image

class JumpBrain():
    def __init__(self):
        self.pixels = []
        self.gameover = []
    
    def jump(self):
        pyautogui.press('space')
    
    def lookahead(self):
        self.pixels = []
        screen = pyautogui.screenshot()
        for x in range(15):
            x_pix = 450 + x
            # x_end = 650 + x
            for y in range(5):
                y_pix = 450 +  y
                # y_end = 400 + y
                self.pixels.append(screen.getpixel((x_pix, y_pix)))
                # self.gameover.append(screen.getpixel((x_end, y_end)))

            
    def timeToJump(self):
        self.lookahead()
        for pix in self.pixels:
            if pix != (247, 247, 247):
                self.jump()
                break
        # for end in self.gameover:
        #     if end != (247, 247, 247):
        #         self.jump()
        #         break
        
            
    def screenshot(self, x):
        name = "my_screenshot" + str(x) + ".png"
        pyautogui.screenshot(name)
