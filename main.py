import sys
import logging
import xml.etree.ElementTree as ET
from shell import Shell

# Функция для загрузки конфигурации из XML
def load_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()
    
    config = {
        'username': root.find('username').text,
        'hostname': root.find('hostname').text,
        'filesystem_path': root.find('filesystem_path').text,  # Путь к архиву
        'log_path': root.find('log_path').text
    }
    return config

def main(config_path):
    # Загружаем конфигурацию
    config = load_config(config_path)
    
    # Настроим логирование
    logging.basicConfig(filename=config['log_path'], level=logging.INFO)
    logger = logging.getLogger()
    
    # Запуск эмулятора
    shell = Shell(config, logger)
    shell.run()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file>")
    else:
        main(sys.argv[1])
