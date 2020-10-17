# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'font_path', 'A4_pixel_size', 'base_path', 'text_path', 'results_path', 'ms_output_path',
           'gcp_output_path', 'aws_output_path', 'text_wrap', 'get_max_line_height', 'get_line_height',
           'get_line_width', 'get_A4_image', 'font_sizes', 'font_size', 'font_file', 'font', 'img', 'left_margin',
           'top_margin', 'right_margin', 'bottom_margin', 'x_right_margin', 'y_bottom_margin', 'printable_width',
           'formats', 'filenames', 'text_files', 'saved_files']

# Cell

#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from textwrap import wrap
from pathlib import Path
import json

# Read a text file and create a clear image of the text on a page.
# Read a text file and create various distorted, transformed or distressed looking page.
# Read an OCR json file from Google and create a clear image of text on a page.
# Read an OCR json file from Google and write a text file of selected areas.

# Set path to fonts
font_path = Path("C:\Windows\fonts")

# Translation from dpi to A4 size
A4_pixel_size = {
    2880: (23811, 33676),
    2400: (19843, 28063),
    1440: (11906, 16838),
    1200: (9921, 14032),
    720:  (5953, 8419),	
    600:  (4960, 7016),
    300:  (2480, 3508),
    150:  (1240, 1754),
    96:   (794, 1123),
    72:   (595, 842)}

# Set paths to texts
base_path = Path("D:\Work\Test\Webbs")
text_path = base_path / "text"
results_path = base_path / "output"
ms_output_path = results_path / "Microsoft"
gcp_output_path = results_path / "Google"
aws_output_path = results_path / "Amazon"

# Cell
def text_wrap(text, font, max_width):
        """Wrap lines to specified width.
        This is to enable text of width more than the image width to be display
        nicely.
        @params:
            text: str
                text to wrap
            font: obj
                font of the text
            max_width: int
                width to split the text with
        @return
            lines: list[str]
                list of sub-strings
        """
        lines = []

        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            words = text.split(' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

# Cell
def get_max_line_height(lines, font):
    # Calculate the height needed to draw each line of text.
    line_heights = [ get_line_height(line,font) for line in lines]
    # Return the maximum line height.
    return max(line_heights)


def get_line_height(line, font):
    # Return the height of a line of text.
    return font.getmask(line).getbbox()[3]


def get_line_width(line, font):
    # Return the width of a line of text.
    return font.getmask(line).getbbox()[2]


def get_A4_image():
    # Set resolution (dpi)
    resolution = 150

    # Set page size in pixels
    A4 = A4_pixel_size[resolution]

    # Create a page sized image
    A4_image = Image.new(mode='RGB', size=A4, color='white')
    return A4_image



# Cell
# Set fonts and sizes.

font_sizes = [10,12,16,18,24]
font_size = 24

font_file = str(font_path / "GentiumPlus-R.ttf")
font = ImageFont.truetype(font_file, font_size)
#font = ImageFont.FreeTypeFont(font_file, font_size)
img = get_A4_image()

left_margin = 40
top_margin = 40
right_margin = 40
bottom_margin = 40

# Get image size in pixels
img_width, img_height = img.size

x_right_margin = img_width - right_margin
y_bottom_margin = img_height - bottom_margin

printable_width = x_right_margin - left_margin
formats = ['jpg','pdf','png','tiff']

filenames = ['bkq-bkqNT.txt','bsq-Bassa02.txt','rbt-psa2-3.txt']
text_files = [text_path / filename for filename in filenames]
print(text_files)

saved_files = []

saved_files.extend(save_multiline_images(text_files,font,formats,printable_width))

print(f'Saved these image files:')
for file in saved_files:
    print(file)
