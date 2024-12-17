import xml.etree.ElementTree as ET

class Config:
    def __init__(self, config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()

        self.username = root.find('username').text
        self.hostname = root.find('hostname').text
        self.filesystem_path = root.find('filesystem_path').text
        self.log_path = root.find('log_path').text
