"""
The `smartfile` package provides utilities for managing, organizing, and processing files. 
It includes functionality for file type identification, metadata extraction, file previewing, 
and bulk renaming.

The public API exposes the following key functions:

Public Functions:
- organize_by_type: Organizes files into directories based on their type (e.g., images, text, etc.).
- get_file_type: Identifies the type of a file by inspecting its extension or content.
- get_metadata: Retrieves metadata from files, such as EXIF data for images or other file attributes.
- preview_image_file: Generates a preview of image files, such as displaying a thumbnail.
- preview_text_file: Provides a preview of text files, displaying the first few lines or characters.
- bulk_rename: Renames multiple files at once based on a provided pattern or rule.

Note: The core functionality is split into various submodules (file_management, file_types, metadata, preview, renaming), 
which are imported and made available here for ease of use.

"""

# Importing functions from submodules
from .file_management import organize_by_type  
from .file_types import get_file_type  
from .metadata import get_metadata 
from .preview import (
    preview_image_file,  
    preview_text_file
)
from .renaming import bulk_rename  # Renames multiple files based on a pattern

# Define the public API of the package by specifying which functions are intended for external use
__all__ = [
    'organize_by_type',   # Organize files into directories based on their type
    'get_file_type',      # Identify file type from extension or content
    'get_metadata',       # Extract file metadata (e.g., EXIF, size)
    'preview_image_file', # Preview image files (e.g., show a thumbnail)
    'preview_text_file',  # Preview text files (e.g., display the first few lines)
    'bulk_rename'         # Bulk rename files according to a specified rule
]