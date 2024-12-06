"""
This module contains functions to generate previews of text and image files.

Functions:
- preview_text_file: Returns a preview of a text file, showing the first few lines.
- preview_image_file: Returns a resized image (thumbnail) preview.

Dependencies:
- PIL (Pillow): Used for handling and manipulating images.
"""

from PIL import Image

def preview_text_file(filepath, num_lines=5):
    """
    Generates a preview of a text file by reading the first few lines.

    Parameters:
    - filepath (str): The path to the text file.
    - num_lines (int): The number of lines to preview (default is 5). 

    Returns:
    - str: A string containing the preview of the text file, with `num_lines` lines.

    Example:
    >>> preview_text_file('/path/to/file.txt', num_lines=3)
    'Line 1 content\nLine 2 content\nLine 3 content'
    """
    with open(filepath, 'r') as file:
        # Read lines and strip any leading/trailing whitespace
        lines = [file.readline().strip() for _ in range(num_lines)]
        # Filters out any empty lines
        lines = [line for line in lines if line]
        # Return the preview by joining the lines with a single newline
        return '\n'.join(lines)

def preview_image_file(filepath):
    """
    Generates a thumbnail preview of an image.

    Parameters:
    - filepath (str): The path to the image file.

    Returns:
    - PIL.Image.Image: A Pillow Image object representing the resized thumbnail.

    Example:
    >>> preview_image_file('/path/to/image.jpg')
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=100x100 at 0x10F4B9B50>
    """
    with Image.open(filepath) as img:
        img.thumbnail((100, 100))  # Resize for preview
        return img