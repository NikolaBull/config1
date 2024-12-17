import os
from filesystem import FileSystem
import logging

class Shell:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.fs = FileSystem(config['filesystem_path'])
        self.current_directory = ''  # Путь к текущей директории в виртуальной файловой системе

    def run(self):
        while True:
            command = input(f"{self.config['username']}@{self.config['hostname']}:{self.current_directory}$ ")

            if command == 'exit':
                self.exit_shell()
            elif command == 'ls':
                self.ls()
            elif command == 'uname':
                self.uname()
            elif command.startswith('cd '):
                self.cd(command)
            elif command.startswith('rm '):
                self.rm(command)
            else:
                print(f"Unknown command: {command}")

    def ls(self):
        """Команда ls для вывода списка файлов в текущей директории."""
        files = self.fs.list_files(self.current_directory)
        if files:
            for file in files:
                print(file)

    def cd(self, command):
        """Команда cd для изменения текущей директории."""
        path = command[3:].strip()  # Убираем "cd " из команды
        if path == "..":
            # Переход на уровень выше
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            # Переход в указанную директорию
            new_path = os.path.join(self.current_directory, path)
            if os.path.isdir(os.path.join(self.fs.extract_folder, new_path)):
                self.current_directory = new_path
            else:
                print(f"Directory '{path}' not found.")
    
    def rm(self, command):
        """Команда rm для удаления файла."""
        file_to_remove = command[3:].strip()  # Убираем "rm " из команды
        file_path = os.path.join(self.fs.extract_folder, self.current_directory, file_to_remove)

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"File {file_to_remove} removed successfully.")
                self.logger.info(f"Removed file: {file_to_remove}")
            except Exception as e:
                print(f"Error removing file {file_to_remove}: {e}")
        else:
            print(f"File '{file_to_remove}' not found.")
    
    def uname(self):
        """Команда uname для вывода информации о системе."""
        print("UNIX Emulator")

    def exit_shell(self):
        """Команда exit для выхода из эмулятора."""
        print("Exiting shell...")
        self.logger.info("Shell session ended.")
        exit(0)
