files = [
    "admin.py",
    "frames.py",
    "main.py",
    "models.py",
    "utils.py"
]

total_lines = 0

for file in files:
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            line_count = sum(1 for _ in f)
            print(f"Файл: {file}, Строк: {line_count}")
            total_lines += line_count
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла {file}: {e}")

print(f"Общее количество строк: {total_lines}")