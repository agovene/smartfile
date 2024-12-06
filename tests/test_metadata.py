import unittest
import os
import tempfile
from PIL import Image
from fpdf import FPDF
from smartfile.metadata import get_metadata

class TestGetMetadata(unittest.TestCase):

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
        with open(file_path, 'wb' if is_binary else 'w') as f:
            f.write(content)
        return file_path

    def test_image_metadata(self):
        """Test retrieving metadata from an image file (PNG)."""
        image_path = os.path.join(self.test_dir.name, 'test_image.png')
        img = Image.new('RGB', (100, 100), color='red')
        img.save(image_path)

        # Get metadata
        metadata = get_metadata(image_path)
        self.assertEqual(metadata["format"], 'PNG')
        self.assertEqual(metadata["size"], (100, 100))
        self.assertEqual(metadata["mode"], 'RGB')

    def test_pdf_metadata(self):
        """Test retrieving metadata from a PDF file."""
        pdf_path = os.path.join(self.test_dir.name, 'test_pdf.pdf')
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Test PDF", ln=True, align="C")
        pdf.output(pdf_path)

        # Get metadata
        metadata = get_metadata(pdf_path)
        self.assertEqual(metadata["num_pages"], 1)  # One page added
        self.assertIsNone(metadata["author"])  # Author is None unless set in FPDF

    def test_other_file_type(self):
        """Test retrieving metadata from a regular text file."""
        text_file_path = self.create_test_file('test_text.txt', "This is a text file.")
        
        # Get metadata
        metadata = get_metadata(text_file_path)
        self.assertEqual(metadata["size"], os.path.getsize(text_file_path))
        self.assertEqual(metadata["created"], os.path.getctime(text_file_path))

    def test_empty_file(self):
        """Test retrieving metadata from an empty file."""
        empty_file_path = self.create_test_file('test_empty.txt', "")
        
        # Get metadata
        metadata = get_metadata(empty_file_path)
        self.assertEqual(metadata["size"], 0)
        self.assertEqual(metadata["created"], os.path.getctime(empty_file_path))

if __name__ == '__main__':
    unittest.main()