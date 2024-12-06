import unittest
import os
import tempfile
from PIL import Image
from smartfile.preview import preview_text_file, preview_image_file

class TestFilePreview(unittest.TestCase):

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

    def create_test_file(self, filename, content, is_binary=False):
        """
        Helper function to create a test file with the given content.
        
        Args:
            filename (str): The name of the file to create.
            content (str or bytes): The content to write to the file.
            is_binary (bool): Whether the content is binary (default False).
            
        Returns:
            str: The path to the created file.
        """
        file_path = os.path.join(self.test_dir.name, filename)
        mode = 'wb' if is_binary else 'w'
        with open(file_path, mode) as f:
            f.write(content)
        return file_path

    def test_text_file_preview(self):
        """Test previewing a text file (first 5 lines)."""
        text_file_path = self.create_test_file('test_text.txt', "\n".join([f"Line {i + 1}" for i in range(10)]))
        
        # Preview first 5 lines
        preview = preview_text_file(text_file_path, num_lines=5)
        expected_preview = "\n".join([f"Line {i + 1}" for i in range(5)])
        self.assertEqual(preview, expected_preview)

    def test_text_file_preview_with_less_lines(self):
        """Test previewing a text file with fewer than 5 lines."""
        text_file_path = self.create_test_file('test_short_text.txt', "\n".join([f"Line {i + 1}" for i in range(3)]))
        
        # Preview should show all 3 lines
        preview = preview_text_file(text_file_path, num_lines=5)
        expected_preview = "\n".join([f"Line {i + 1}" for i in range(3)])
        self.assertEqual(preview, expected_preview)

    def test_image_file_preview(self):
        """Test previewing an image file (resize to 100x100)."""
        image_path = os.path.join(self.test_dir.name, 'test_image.png')
        img = Image.new('RGB', (200, 200), color='blue')
        img.save(image_path)

        # Test preview image (resize to thumbnail)
        preview_img = preview_image_file(image_path)

        # Check if image was resized to 100x100
        self.assertEqual(preview_img.size, (100, 100))

    def test_image_file_preview_small_image(self):
        """Test previewing a small image file (should not resize)."""
        image_path = os.path.join(self.test_dir.name, 'small_image.png')
        img = Image.new('RGB', (50, 50), color='red')
        img.save(image_path)

        # Preview should remain the same as the original size
        preview_img = preview_image_file(image_path)
        self.assertEqual(preview_img.size, (50, 50))

    def test_nonexistent_file(self):
        """Test previewing a non-existent file (should raise FileNotFoundError)."""
        non_existent_path = os.path.join(self.test_dir.name, 'non_existent_file.txt')
        
        # Test previewing a non-existent text file
        with self.assertRaises(FileNotFoundError):
            preview_text_file(non_existent_path)
        
        # Test previewing a non-existent image file
        with self.assertRaises(FileNotFoundError):
            preview_image_file(non_existent_path)

if __name__ == '__main__':
    unittest.main()