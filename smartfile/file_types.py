import os
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

    Raises:
    - TypeError: If the filepath is not a string, bytes, or os.PathLike object.
    - FileNotFoundError: If the file does not exist.
    - ValueError: If the filepath points to a directory instead of a file.

    Example:
    >>> get_file_type('/path/to/file.jpg')
    'image/jpeg'
    """
    # Validate input type
    if not isinstance(filepath, (str, bytes, os.PathLike)):
        raise TypeError(f"Invalid type for filepath: {type(filepath).__name__}")

    # Check if the file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")

    # Check if the path is a directory
    if os.path.isdir(filepath):
        raise ValueError(f"The path '{filepath}' is a directory, not a file.")

    # Try using mimetypes to guess based on file extension
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type:
        return mime_type

    # If mimetypes failed, fall back to filetype for binary inspection
    kind = filetype.guess(filepath)
    if kind:
        return kind.mime

    return None