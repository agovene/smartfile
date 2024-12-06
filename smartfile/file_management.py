"""
This module contains functions for organizing files within a directory based on their type.

The primary function exposed by this module is `organize_by_type`, which moves files into
subdirectories based on the file type (e.g., 'image', 'text', 'audio').

Functions:
- organize_by_type: Organizes files in the specified directory by moving them into subdirectories 
  named after their type (e.g., 'image', 'text', etc.).

Dependencies:
- This module relies on the `get_file_type` function from the `smartfile.file_types` submodule to 
  determine the file type based on its content or extension.
"""

import os
import shutil
from smartfile.file_types import get_file_type

def organize_by_type(directory):
    """
    Organizes files in the specified directory by type. This function scans the given directory, 
    identifies the type of each file, and moves it into a subdirectory based on its type.

    Parameters:
    - directory (str): The path to the directory that contains the files to be organized.

    Raises:
    - ValueError: If the specified directory does not exist.
    
    Example usage:
    >>> organize_by_type('/path/to/directory')
    This will organize all files in '/path/to/directory' by type into appropriate subdirectories.
    """
    
    # Check if the provided directory exists
    if not os.path.exists(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Only process files (not subdirectories)
        if os.path.isfile(filepath):
            file_type = get_file_type(filepath)
            
            if file_type:
                subfolder = file_type.split('/')[0]  # Example: 'image', 'text'
                subfolder_path = os.path.join(directory, subfolder)
                
                # Create the subfolder if it doesn't already exist
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                    
                # Move the file to the appropriate subfolder
                shutil.move(filepath, os.path.join(subfolder_path, filename))