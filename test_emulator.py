import os
import shutil
import subprocess

CONFIG_PATH = "config.xml"

def prepare_filesystem():
    """Подготовить файловую систему перед каждым тестом."""
    if os.path.exists("extracted_files"):
        shutil.rmtree("extracted_files")
    if os.path.exists("filesystem.zip"):
        shutil.copy("filesystem_backup.zip", "filesystem.zip")

def execute_command(command):
    """Выполнить команду в оболочке и вернуть результат."""
    process = subprocess.Popen(
        ["python", "main.py", CONFIG_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input=command + "\nexit\n")
    return stdout

def test_ls():
    prepare_filesystem()
    stdout = execute_command("ls")
    # Проверяем, что команда ls возвращает какой-либо вывод
    assert "file1.txt" in stdout or "dir1" in stdout, "Команда ls не вернула ожидаемый результат."
    print("Тест ls пройден: ls работает!")

def test_cd():
    prepare_filesystem()
    stdout = execute_command("cd dir1")
    # Проверяем, что команда cd не выдает ошибок
    assert "nested_file.txt" in stdout or "dir2" in stdout, "Команда cd не вернула ожидаемый результат."
    print("Тест cd пройден: cd работает!")

def test_rm():
    prepare_filesystem()
    # Убедимся, что файл file1.txt существует перед удалением
    stdout = execute_command("ls")
    assert "file1.txt" in stdout, "Файл file1.txt не найден перед удалением."

    # Удаляем файл
    execute_command("rm file1.txt")
    
    # Проверяем, что файл file1.txt был удален
    stdout = execute_command("ls")
    assert "file1.txt" not in stdout, "Файл file1.txt не был удален."
    print("Тест rm пройден: rm работает!")

def test_uname():
    stdout = execute_command("uname")
    # Проверяем, что команда uname выводит правильный результат
    assert "UNIX Emulator" in stdout, "Команда uname не вернула правильный результат."
    print("Тест uname пройден: uname работает!")

def test_exit():
    stdout = execute_command("exit")
    # Проверяем, что команда exit завершает сессию
    assert "Exiting shell..." in stdout, "Команда exit не завершила сессию корректно."
    print("Тест exit пройден: exit работает!")

if __name__ == "__main__":
    test_ls()
    test_cd()
    test_rm()
    test_uname()
    test_exit()
