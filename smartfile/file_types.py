"""
This module contains the function `get_file_type` that determines the MIME type of a file 
based on its extension and/or content.

Functions:
- get_file_type: Returns the MIME type of a file by first checking its extension using mimetypes, 
  and then inspecting its contents using the `filetype` library if necessary.

Dependencies:
- mimetypes: Used for guessing MIME types based on file extensions.
- filetype: Used for binary inspection of files when mimetypes is insufficient.
"""

import mimetypes
import filetype

def get_file_type(filepath):
    """
    Determines the MIME type of a file by inspecting its extension or content.

    The function first tries to guess the MIME type based on the file's extension using the
    `mimetypes` library. If that fails, it falls back on the `filetype` library, which inspects 
    the file's contents to guess its MIME type.

    Parameters:
    - filepath (str): The path to the file whose MIME type is to be determined.

    Returns:
    - str: The MIME type of the file (e.g., 'image/jpeg', 'text/plain'), or None if the type 
      cannot be determined.

    Example:
    >>> get_file_type('/path/to/file.jpg')
    'image/jpeg'
    """
    
    # Try using mimetypes to guess based on file extension
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type:
        return mime_type

    # If mimetypes failed, fall back to filetype for binary inspection
    kind = filetype.guess(filepath)
    if kind:
        return kind.mime
    
    # Return None if the file type couldn't be determined
    return None