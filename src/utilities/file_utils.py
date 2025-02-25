import json
import yaml
import os
from dotenv import load_dotenv

class ConfigReader:
    def __init__(self):
        load_dotenv()
        self.config_path= os.path.join(os.path.dirname(__file__), '../../config/config.yaml')
        self.test_data_path= os.path.join(os.path.dirname(__file__), '../test_data/test_payloads.json')


        with open(self.config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self, env):
        """
        Get configuartion for specific environment
        :param env: environment name (dev, prod, etc)
        :return: dictionary with configuration
        """

        env_config =  self.config['environments'].get(env, {})
        # Replace environment variables
        for key, value in env_config.items():
            if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
                env_var = value[2:-1]
                env_config[key] = os.getenv(env_var)
        return env_config
    
    def get_test_payload(self, payload_type):
        """
        Get Test Payload by type
        :param payload_type: type of payload (user_creation, product_creation, etc)
        :return: dictionary with payload
        """
        with open(self.test_data_path, 'r') as file:
            payloads = json.load(file)
        return payloads.get(payload_type, {})
class FileHandler:
    @staticmethod
    def read_json(file_path):
        """
        """
        with open(file_path, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def write_json(file_path):
        """
        """
        with open(file_path, 'r') as file:
            return json.dump(data, file, indent=4)
        
    @staticmethod
    def read_file(file_path):
        """
        """
        with open(file_path, 'r') as file:
            return file.read()
        
    @staticmethod
    def write_file(file_path, content):
        """
        """
        with open(file_path, 'r') as file:
            file.write(content)