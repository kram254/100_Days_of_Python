import io
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg

def create_new_year_image():
    """
    Happy New Year 2023 image using Pillow.
    """
    # Create a blank image with a white background
    image = Image.new("RGB", (400, 100), (255, 255, 255))

    # drawing context
    draw = ImageDraw.Draw(image)

    # font
    font = ImageFont.truetype("arial.ttf", 36)

    # Drawing the text on the image
    text = "Happy New Year 2023"
    text_width, text_height = draw.textsize(text, font=font)
    x = (400 - text_width) // 2
    y = (100 - text_height) // 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))

    # Save the image to a memory buffer
    buffer = io.BytesIO()
    image.save(buffer, "png")

    # Rewinding the buffer and return the image data
    buffer.seek(0)
    return buffer.read()

def show_new_year_presentation():
    """
    Happy New Year 2023 presentation using PySimpleGUI.
    """
    # Create the layout for the presentation window
    layout = [[sg.Image(data=create_new_year_image())]]

    # Create the window
    window = sg.Window("Happy New Year 2023", layout)

    # Show the window and wait for the user to close it
    event, values = window.read()
    window.close()

def main():
    show_new_year_presentation()

if __name__ == "__main__":
    main()
