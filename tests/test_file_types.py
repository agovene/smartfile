import unittest
import os
import tempfile
from smartfile.file_types import get_file_type

class TestGetFileType(unittest.TestCase):

    def setUp(self):
        """
        Set up a temporary directory for testing.
        This directory will be used to create files for each test case.
        """
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        """
        Clean up the temporary directory after each test.
        """
        self.test_dir.cleanup()

    def create_test_file(self, filename, content):
        """
        Helper function to create a file with the given content in the test directory.
        
        Args:
            filename (str): The name of the file.
            content (str or bytes): Content to write to the file.
        """
        file_path = os.path.join(self.test_dir.name, filename)
        with open(file_path, 'wb' if isinstance(content, bytes) else 'w') as f:
            f.write(content)
        return file_path

    def test_txt_file(self):
        """Test getting MIME type for a .txt file."""
        file_path = self.create_test_file('test.txt', "This is a text file.")
        result = get_file_type(file_path)
        self.assertEqual(result, 'text/plain')

    def test_jpg_file(self):
        """Test getting MIME type for a .jpg file."""
        file_path = self.create_test_file('test.jpg', b'\xff\xd8\xff\xe0\x00\x10JFIF')
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/jpeg')

    def test_png_file(self):
        """Test getting MIME type for a .png file."""
        file_path = self.create_test_file('test.png', b'\x89PNG\r\n\x1a\n')
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/png')

    def test_unknown_extension(self):
        """Test getting MIME type for a file with an unknown extension."""
        file_path = self.create_test_file('test.abc', "This file has an unknown extension.")
        result = get_file_type(file_path)
        self.assertIsNone(result)  # Should return None for unknown types

    def test_no_extension(self):
        """Test getting MIME type for a file with no extension but valid binary content."""
        file_path = self.create_test_file('testfile', b'\x89PNG\r\n\x1a\n')  # PNG header
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/png')

if __name__ == '__main__':
    unittest.main()
