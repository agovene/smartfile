# SmartFile

SmartFile is a simple Python package designed to help you manage and organize files more efficiently. It provides basic tools for sorting files by type, renaming files in bulk, extracting metadata from image and PDF files, and previewing the contents of text and image files. While it’s not a complex solution yet, SmartFile makes it easier to automate some of the most common file-handling tasks.

## Features

- **Organize files by type**: Automatically organize files in a directory based on their MIME type.
- **Bulk renaming**: Rename files in bulk by adding a custom prefix or default naming convention.
- **Metadata extraction**: Extract metadata from image files (JPEG, PNG) and PDF files.
- **File previews**: Preview the content of text files (first few lines) and image files (resized thumbnails).

## Installation

You can install the `smartfile` package via the GitHub repository:

```bash
pip install git+https://github.com/yourusername/smartfile.git
```

## Usage

Here are some examples of how to use the core features of smartfile.

### Organize Files by Type

```python
from smartfile import organize_by_type
```

#### Organize files in the specified directory by their MIME type.

```python
organize_by_type('/path/to/directory')
```

This function will organize files in the given directory into subfolders based on their file types (e.g., image, text, audio).

### Bulk Rename Files

```python
from smartfile import bulk_rename
```

#### Rename all files in a directory with a custom prefix.

```python
new_names = bulk_rename('/path/to/directory', prefix='new_')
print(new_names)  # List of renamed files
```

This function renames all files in the specified directory by adding a numeric prefix to each file.

### Extract Metadata from Files

Image Metadata (JPEG, PNG)

```python
from smartfile import get_metadata
```

#### Get metadata for an image file.

```python
metadata = get_metadata('/path/to/image.jpg')
print(metadata)  # Example: {'format': 'JPEG', 'size': (1024, 768), 'mode': 'RGB'}
```

#### Get metadata for a PDF file.

```python
metadata = get_metadata('/path/to/file.pdf')
print(metadata)  # Example: {'author': 'John Doe', 'num_pages': 5}
```

### Preview File Content

Preview Text File

```python
from smartfile import preview_text_file
```
#### Preview the first 5 lines of a text file.

```python
preview = preview_text_file('/path/to/file.txt', num_lines=5)
print(preview)
```

### Preview Image File

```python
from smartfile import preview_image_file
```

#### Preview an image file (thumbnail resized to 100x100).

```python
preview_img = preview_image_file('/path/to/image.jpg')
preview_img.show()
```

## Contributing

We welcome contributions to smartfile! If you'd like to contribute, here are a few guidelines:

    Fork the repository: Create a fork of the repository on GitHub.
    Clone your fork: Clone your fork to your local machine and create a feature branch.
    Write tests: If you're adding new features or fixing bugs, please add appropriate tests.
    Make your changes: Implement the changes or features you want to contribute.
    Submit a Pull Request: Once you're done, submit a pull request to the main branch.

We follow the PEP 8 style guide for Python code, and contributions should adhere to it.

## License

SmartFile is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

    Pillow: For image handling and metadata extraction.
    PyPDF2: For PDF metadata extraction.
    Filetype: For MIME type detection.

## Contact

    Author: Arnaldo Govene
    Email: arnaldo.govene@outlook.com
    GitHub: https://github.com/agovene/smartfile