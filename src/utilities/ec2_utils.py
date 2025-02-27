import paramiko

from utilities.file_utils import ConfigReader

class EC2Connection:
    def __init__(self):
        config = ConfigReader().get_config('ec2')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            hostname='ec2-host',
            username=config['username'],
            key_filename=config['key-path']
        )

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode()
    
    def close(self):
        self.ssh.close()