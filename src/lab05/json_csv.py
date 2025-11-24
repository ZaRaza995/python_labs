import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл (список словарей) в CSV-файл.
    """
    json_p = Path(json_path)
    csv_p = Path(csv_path)
    # --- Проверки входных данных ---
    if (
        not json_p.is_file()
    ):  # is_file() сразу проверяет, что это файл, а не папка, и что он существует
        raise FileNotFoundError(f"Файл не найден или это папка: {json_path}")

    # Проверка расширения файла - это должен быть .json файл
    if json_p.suffix.lower() != ".json":
        raise ValueError(
            f"Файл должен иметь расширение .json, получено: {json_p.suffix} (файл: {json_p.name})"
        )

    if json_p.stat().st_size == 0:
        raise ValueError(f"JSON-файл пуст: {json_path}")
    # --- Чтение и обработка ---
    try:
        with json_p.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Некорректный синтаксис в JSON-файле: {json_path}")

    if not isinstance(data, list) or not data:
        raise ValueError("JSON должен содержать непустой список.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы в JSON-списке должны быть словарями.")
    # Собираем все уникальные заголовки
    headers = set()
    for item in data:
        headers.update(item.keys())
    sorted_headers = sorted(list(headers))

    # Запись в CSV
    csv_p.parent.mkdir(parents=True, exist_ok=True)
    with csv_p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sorted_headers)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV-файл в JSON-файл (список словарей).
    """
    csv_p = Path(csv_path)
    json_p = Path(json_path)
    # --- Проверки входных данных ---
    if not csv_p.is_file():
        raise FileNotFoundError(f"Файл не найден или это папка: {csv_path}")

    # Проверка расширения файла - это должен быть .csv файл
    if csv_p.suffix.lower() != ".csv":
        raise ValueError(
            f"Файл должен иметь расширение .csv, получено: {csv_p.suffix} (файл: {csv_p.name})"
        )
    # --- Чтение и обработка ---
    data = []
    with csv_p.open("r", encoding="utf-8", newline="") as f:
        # DictReader - лучший инструмент для этой задачи
        reader = csv.DictReader(f)
        # Если в файле нет первой строки (заголовка), fieldnames будет None или []
        if not reader.fieldnames:
            raise ValueError(f"CSV-файл пуст или не содержит заголовка: {csv_path}")
        # Просто и эффективно преобразуем все строки в список словарей
        data = list(reader)
    # Запись в JSON
    json_p.parent.mkdir(parents=True, exist_ok=True)
    with json_p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Пример использования: обновление всех файлов из people.json
    json_input = "src/data/lab05/samples/people.json"
    csv_output = "src/data/lab05/out/people_from_json.csv"
    json_output = "src/data/lab05/out/people_from_csv.json"

    try:
        print(f"Обновление файлов из {json_input}")

        # JSON → CSV
        json_to_csv(json_input, csv_output)
        print(f" Создан {csv_output}")

        # CSV → JSON (проверка обратной конвертации)
        csv_to_json(csv_output, json_output)
        print(f" Создан {json_output}")

        print("\nВсе файлы обновлены!")
    except Exception as e:
        print(f"Ошибка: {e}")
