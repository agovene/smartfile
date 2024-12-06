import os
import unittest
import tempfile
from smartfile.renaming import bulk_rename

class TestBulkRename(unittest.TestCase):

    def setUp(self):
        """
        Set up a temporary directory with sample files for renaming.
        """
        self.test_dir = tempfile.TemporaryDirectory()
        self.create_test_files()

    def create_test_files(self):
        """
        Helper function to create sample files for renaming.
        """
        for i in range(5):
            file_path = os.path.join(self.test_dir.name, f"testfile_{i}.txt")
            with open(file_path, 'w') as f:
                f.write(f"Sample content for file {i}")

    def test_bulk_rename_with_custom_prefix(self):
        """
        Test the bulk renaming functionality with a custom prefix.
        """
        new_file_names = bulk_rename(self.test_dir.name, prefix='new_file_')

        # Check if the renamed files exist and match the expected pattern
        for idx, new_name in enumerate(new_file_names):
            new_file_path = os.path.join(self.test_dir.name, new_name)
            self.assertTrue(os.path.exists(new_file_path), f"File {new_file_path} does not exist.")
            self.assertTrue(new_name.startswith('new_file_'), f"File {new_name} does not start with the expected prefix.")

    def test_bulk_rename_without_prefix(self):
        """
        Test the bulk renaming functionality with the default prefix.
        """
        new_file_names = bulk_rename(self.test_dir.name)

        # Check if the renamed files exist and match the expected pattern
        for idx, new_name in enumerate(new_file_names):
            new_file_path = os.path.join(self.test_dir.name, new_name)
            self.assertTrue(os.path.exists(new_file_path), f"File {new_file_path} does not exist.")
            self.assertTrue(new_name.startswith('file_'), f"File {new_name} does not start with the expected prefix.")

    def tearDown(self):
        """
        Clean up the temporary directory and files after the test.
        """
        # Cleanup the files in the temporary directory
        for filename in os.listdir(self.test_dir.name):
            file_path = os.path.join(self.test_dir.name, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        self.test_dir.cleanup()

if __name__ == '__main__':
    unittest.main()