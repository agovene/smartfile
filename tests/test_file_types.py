import unittest
import os
import tempfile
from smartfile.file_types import get_file_type

class TestGetFileType(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def create_test_file(self, filename, content):
        file_path = os.path.join(self.test_dir.name, filename)
        with open(file_path, 'wb' if isinstance(content, bytes) else 'w') as f:
            f.write(content)
        return file_path

    def test_txt_file(self):
        file_path = self.create_test_file('test.txt', "This is a text file.")
        result = get_file_type(file_path)
        self.assertEqual(result, 'text/plain')

    def test_jpg_file(self):
        file_path = self.create_test_file('test.jpg', b'\xff\xd8\xff\xe0\x00\x10JFIF')
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/jpeg')

    def test_png_file(self):
        file_path = self.create_test_file('test.png', b'\x89PNG\r\n\x1a\n')
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/png')

    def test_pdf_file(self):
        file_path = self.create_test_file('test.pdf', b'%PDF-1.4')
        result = get_file_type(file_path)
        self.assertEqual(result, 'application/pdf')

    def test_unknown_extension(self):
        file_path = self.create_test_file('test.abc', "Unknown extension content.")
        result = get_file_type(file_path)
        self.assertIsNone(result)

    def test_no_extension(self):
        file_path = self.create_test_file('testfile', b'\x89PNG\r\n\x1a\n')
        result = get_file_type(file_path)
        self.assertEqual(result, 'image/png')

    def test_empty_file(self):
        file_path = self.create_test_file('empty.txt', "")
        result = get_file_type(file_path)
        self.assertEqual(result, 'text/plain')  

    def test_directory_path(self):
        with self.assertRaises(ValueError):
            get_file_type(self.test_dir.name)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            get_file_type(os.path.join(self.test_dir.name, 'nonexistent.txt'))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_file_type(None)

    def test_binary_file_with_no_mime(self):
        file_path = self.create_test_file('binaryfile.bin', b'\x00\x01\x02\x03')
        result = get_file_type(file_path)
        self.assertEqual(result, 'application/octet-stream')

if __name__ == '__main__':
    unittest.main()