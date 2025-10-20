import csv  # Модуль для работы с CSV-файлами (чтение и запись таблиц)
from pathlib import Path  # Удобный способ работать с путями к файлам и папкам
from typing import Sequence  # Используется для подсказки типов (списки, кортежи и т.д.)

def ensure_parent_dir(path: str | Path) -> None:
    # Преобразуем переданный путь в объект Path, чтобы удобно работать с ним
    # Получаем родительскую папку файла
    # Если папка не существует, создаём её
    # parents=True — создаёт все промежуточные папки
    # exist_ok=True — не вызывает ошибку, если папка уже существует
    parent_directory = Path(path).parent
    parent_directory.mkdir(parents=True, exist_ok=True)

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    # Преобразуем путь в объект Path
    # С помощью метода read_text читаем весь текст из файла
    # encoding="utf-8" гарантирует правильное чтение русских символов и Unicode
    # Возвращаем весь текст файла как строку
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Sequence[Sequence], path: str | Path, header: Sequence[str] | None = None) -> None:
    # Убеждаемся, что папка для файла существует, иначе запись вызовет ошибку
    ensure_parent_dir(path)

    # Если есть строки для записи, проверяем, что все строки одной длины
    # Это важно, потому что CSV — таблица, и все строки должны иметь одинаковое количество столбцов
    if rows:
        expected_len = len(rows[0])  # Сколько элементов в первой строке
        if not all(len(row) == expected_len for row in rows):  # Проверка остальных строк
            raise ValueError("Все строки для записи в CSV должны иметь одинаковую длину.")

    # Создаём объект Path для файла
    p = Path(path)

    # Открываем файл для записи
    # "w" — режим записи (файл будет перезаписан, если существует)
    # newline="" — чтобы не вставлялись лишние пустые строки между записями
    # encoding="utf-8" — сохраняем текст в UTF-8
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)  # Создаём объект writer для записи CSV
        
        # Если есть заголовок — записываем его первой строкой
        if header:
            writer.writerow(header)

        # Записываем все строки данных
        writer.writerows(rows)
