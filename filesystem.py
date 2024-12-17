import os
import zipfile

class FileSystem:
    def __init__(self, filesystem_path):
        self.filesystem_path = filesystem_path
        self.extract_folder = 'extracted_files'  # Папка для распакованных файлов

        # Если папка для извлечения файлов не существует, создаем ее
        if not os.path.exists(self.extract_folder):
            os.makedirs(self.extract_folder)

        # Распаковываем архив
        self._load_filesystem()

    def _load_filesystem(self):
        """Распаковываем архив файловой системы."""
        if zipfile.is_zipfile(self.filesystem_path):
            with zipfile.ZipFile(self.filesystem_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_folder)
        else:
            print(f"Error: {self.filesystem_path} is not a valid zip file.")

    def list_files(self, path):
        """Возвращает список файлов и папок в указанной директории."""
        full_path = os.path.join(self.extract_folder, path)
        try:
            return os.listdir(full_path)
        except FileNotFoundError:
            print(f"Directory '{path}' not found.")
            return []
