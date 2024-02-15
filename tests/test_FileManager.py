import unittest
from unittest.mock import mock_open, patch
from FileManager import FileManager
import os
import json

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file_manager = FileManager()

    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_load_data(self, mock_file_open):
        result = self.file_manager.load_data('test.txt')
        mock_file_open.assert_called_once_with('test.txt', 'r')
        self.assertEqual(result, '{"key": "value"}')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data(self, mock_file_open):
        self.file_manager.save_data('test.txt', 'data to save')
        mock_file_open.assert_called_once_with('test.txt', 'w')
        mock_file_open().write.assert_called_once_with('data to save')

    @patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
    def test_read_json(self, mock_file_open):
        result = self.file_manager.read_json('test.json')
        mock_file_open.assert_called_once_with('test.json', 'r')
        self.assertEqual(result, [{"key": "value"}])

    def test_write_json(self):
        test_data = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]
        self.file_manager.write_json(test_data, "test.json")
        self.assertTrue(os.path.exists("test.json"))
        with open("test.json", 'r') as file:
            loaded_data = json.load(file)
            self.assertEqual(loaded_data, test_data)

    @patch('FileManager.FileManager.read_json')
    @patch('FileManager.FileManager.write_json')
    def test_add_to_json(self, mock_write_json, mock_read_json):
        mock_read_json.return_value = [{"existing_key": "existing_value"}]
        self.file_manager.add_to_json({"new_key": "new_value"}, 'test.json')
        mock_read_json.assert_called_once_with('test.json')
        mock_write_json.assert_called_once_with([{"existing_key": "existing_value"}, {"new_key": "new_value"}], 'test.json')

if __name__ == '__main__':
    unittest.main()
