import os
import unittest
from src.utilities.file_utils import ConfigReader

class TestConfigReader(unittest.TestCase):
    def setUp(self):
        # Initialize the ConfigReader instance
        self.config_reader = ConfigReader()

    def test_get_config_valid_env(self):
        # Test fetching configuration for a valid environment
        config = self.config_reader.get_config('dev')
        self.assertIsInstance(config, dict)
        self.assertIn('timeout', config)
        self.assertIn('retry_attempts', config)

    def test_get_config_invalid_env(self):
        # Test fetching configuration for an invalid environment
        config = self.config_reader.get_config('invalid_env')
        self.assertEqual(config, {})

    def test_get_test_payload_valid_type(self):
        # Test fetching test payload for a valid type
        payload = self.config_reader.get_test_payload('user_creation')
        self.assertIsInstance(payload, dict)

    def test_get_test_payload_invalid_type(self):
        # Test fetching test payload for an invalid type
        payload = self.config_reader.get_test_payload('invalid_type')
        self.assertEqual(payload, {})

if __name__ == '__main__':
    unittest.main()