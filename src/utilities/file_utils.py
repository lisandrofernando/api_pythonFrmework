import json
import yaml
import os
from dotenv import load_dotenv

# Load the config.yaml file once and make it reusable
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../../config/config.yaml')

def load_config():
    """
    Load the configuration from the config.yaml file.
    :return: Dictionary containing the configuration.
    """
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)

class ConfigReader:
    def __init__(self):
        load_dotenv()
        self.config = load_config()
        self.test_data_path = os.path.join(os.path.dirname(__file__), '../test_data/test_payloads.json')

    def get_config(self, env):
        """
        Get configuration for a specific environment.
        :param env: Environment name (dev, prod, etc).
        :return: Dictionary with configuration.
        """
        env_config = self.config['environments'].get(env, {})
        # Replace environment variables
        for key, value in env_config.items():
            if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
                env_var = value[2:-1]
                env_config[key] = os.getenv(env_var)
        return env_config

    def get_test_payload(self, payload_type):
        """
        Get Test Payload by type.
        :param payload_type: Type of payload (user_creation, product_creation, etc).
        :return: Dictionary with payload.
        """
        with open(self.test_data_path, 'r') as file:
            payloads = json.load(file)
        return payloads.get(payload_type, {})

class FileHandler:
    @staticmethod
    def read_json(file_path):
        """
        Read JSON data from a file.
        :param file_path: Path to the file.
        :return: Parsed JSON data.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        """
        Write JSON data to a file.
        :param file_path: Path to the file.
        :param data: Data to be written to the file.
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_file(file_path):
        """
        Read the content of a file.
        :param file_path: Path to the file.
        :return: File content as a string.
        """
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """
        Write content to a file.
        :param file_path: Path to the file.
        :param content: Content to be written.
        """
        with open(file_path, 'w') as file:  # Fixed the mode to 'w' for writing
            file.write(content)