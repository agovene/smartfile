import unittest
import os
from smartfile.file_management import organize_by_type
from smartfile.file_types import get_file_type

class TestFileManagement(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test directory and create test files of different types.
        """
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create mock test files with different types
        self.files = [
            'image1.jpg',  # image file
            'document1.pdf',  # pdf file
            'text1.txt',  # text file
            'audio1.mp3'  # audio file
        ]
        
        for file_name in self.files:
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write(f"Sample content for {file_name}")
    
    def test_organize_by_type(self):
        """
        Test that files are organized correctly by type (e.g., images, text, pdfs, etc.).
        """
        # Run the organize_by_type function
        organize_by_type(self.test_dir)
        
        # Check if the files have been moved to the correct subdirectories
        for file_name in self.files:
            file_path = os.path.join(self.test_dir, file_name)
            file_type = get_file_type(file_path)  # Use get_file_type to get the MIME type
            
            # Subdirectory name should match the type (image, text, pdf, etc.)
            subfolder = file_type.split('/')[0] if file_type else 'unknown'
            subfolder_path = os.path.join(self.test_dir, subfolder)
            
            # Assert that the file is moved to the correct subfolder
            self.assertTrue(os.path.exists(os.path.join(subfolder_path, file_name)), 
                            f"{file_name} should be in the {subfolder} folder.")
    
    def tearDown(self):
        """
        Clean up test directory by removing all files and subdirectories.
        """
        # Remove all files and subdirectories
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        
        # Remove the test directory itself
        os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()