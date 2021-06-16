from PIL import ImageFont

height = 240
width = 240

BLACK = (1, 1, 1)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
CENTER = 5
LOOP = 6  # not a key but screen refresh
INIT = 7 # dummy function to flag first call
CONFIRM = 8 # flag for in confirm screen

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

HALF_CHAR =16 # aprox half the width of a character - used for centering
