"""
Module for bulk renaming files in a directory by adding a prefix and a numerical index.

Dependencies:
- os: For file system operations (e.g., renaming files).
"""

import os

def bulk_rename(directory, prefix='file_'):
    """
    Renames files in the specified directory by adding a prefix and a numerical index.

    Args:
        directory (str): Path to the directory.
        prefix (str): Prefix to prepend to each file. Defaults to 'file_'.

    Returns:
        list: List of new file names for renamed files.

    Raises:
        ValueError: If the directory is invalid.

    Example:
        >>> bulk_rename('/path/to/files', 'image_')
        ['image_1_file1.jpg', 'image_2_file2.png']
    """
    new_file_names = []
    
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a valid directory.")
    
    for idx, filename in enumerate(os.listdir(directory)):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            new_name = f"{prefix}{idx+1}_{filename}"
            new_filepath = os.path.join(directory, new_name)
            try:
                os.rename(filepath, new_filepath)
                new_file_names.append(new_name)
            except OSError as e:
                print(f"Error renaming {filename}: {e}")
    
    return new_file_names