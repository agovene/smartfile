"""
This module provides functions to extract metadata from different types of files, including
images and PDFs.

Functions:
- get_image_metadata: Extracts metadata from image files (e.g., format, size, and mode).
- get_pdf_metadata: Extracts metadata from PDF files (e.g., author, number of pages).
- get_metadata: A general function that determines the metadata for a given file, 
  supporting image and PDF files as well as other file types.

Dependencies:
- PIL (Pillow): Used for working with image files.
- PyPDF2: Used for extracting metadata from PDF files.
- os: Used for basic file system operations such as file size and creation time.
"""

import os
from PIL import Image
from PyPDF2 import PdfReader

def get_image_metadata(filepath):
    """
    Extracts metadata from an image file.

    Parameters:
    - filepath (str): The path to the image file.

    Returns:
    - dict: A dictionary containing the image's format, size (as a tuple), and color mode.
    
    Example:
    >>> get_image_metadata('/path/to/image.jpg')
    {'format': 'JPEG', 'size': (1920, 1080), 'mode': 'RGB'}
    """
    with Image.open(filepath) as img:
        return {
            "format": img.format,
            "size": img.size,
            "mode": img.mode
        }

def get_pdf_metadata(filepath):
    """
    Extracts metadata from a PDF file.

    Parameters:
    - filepath (str): The path to the PDF file.

    Returns:
    - dict: A dictionary containing the PDF's author and number of pages.
    
    Example:
    >>> get_pdf_metadata('/path/to/document.pdf')
    {'author': 'John Doe', 'num_pages': 10}
    """
    with open(filepath, 'rb') as f:
        reader = PdfReader(f) 
        return {
            "author": reader.metadata.get('author', None),  # Return 'None' if no author
            "num_pages": len(reader.pages)
        }

def get_metadata(filepath):
    """
    Retrieves metadata from a file based on its type (image, PDF, or general file).

    Parameters:
    - filepath (str): The path to the file.

    Returns:
    - dict: A dictionary containing metadata relevant to the file type.
      - For images, it includes format, size, and mode.
      - For PDFs, it includes author and number of pages.
      - For other file types, it includes size and creation time.
    
    Example:
    >>> get_metadata('/path/to/image.jpg')
    {'format': 'JPEG', 'size': (1920, 1080), 'mode': 'RGB'}
    >>> get_metadata('/path/to/document.pdf')
    {'author': 'John Doe', 'num_pages': 10}
    >>> get_metadata('/path/to/otherfile.txt')
    {'size': 1024, 'created': 1622548695}
    """
    if filepath.endswith('.jpg') or filepath.endswith('.png'):
        return get_image_metadata(filepath)
    elif filepath.endswith('.pdf'):
        return get_pdf_metadata(filepath)
    else:
        return {
            "size": os.path.getsize(filepath),
            "created": os.path.getctime(filepath)
        }