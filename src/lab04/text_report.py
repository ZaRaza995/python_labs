import sys  # Для работы с системными функциями (например, выход из программы)
import os  # Для работы с путями и файловой системой

# Добавляем корневую папку проекта в список путей поиска модулей
# Нужно, чтобы Python видел наши локальные модули (lab04, lib)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Импортируем функции для работы с файлами и обработки текста
from lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq_manual, top_n

# Пути к входному тексту и выходному CSV-отчету
input_path = "src/data/lab04/input.txt"
output_path = "src/data/lab04/report.csv"

try:
    # Читаем текст из файла
    text = read_text(input_path)

    # Обработка текста: нормализация → токенизация → подсчет частот
    freq = count_freq_manual(tokenize(normalize(text)))

    # Если текст пустой или не содержит слов — выводим сообщение и выходим
    if not freq:
        print("Входной файл пуст или не содержит слов. Отчёт не будет создан.")
        sys.exit(0)

    # Запись отчета в CSV
    # sorted() — сортируем по убыванию частоты, при равных — по алфавиту
    # header — первая строка файла с названиями столбцов
    write_csv(
        sorted(freq.items(), key=lambda x: (-x[1], x[0])),
        output_path,
        header=("word", "count"),
    )

    # Выводим статистику в консоль
    print(f"Слов: {sum(freq.values())}, Уникальных: {len(freq)}")
    # Выводим топ-5 самых частых слов
    print("Топ-5:", *[f"{w}:{c}" for w, c in top_n(freq, 5)])
    print(f"\nОтчёт успешно сохранён в файл: {output_path}")

# Если входной файл не найден — выводим сообщение об ошибке и выходим с кодом 1
except FileNotFoundError:
    print(f"Ошибка: Входной файл не найден по пути '{input_path}'")
    sys.exit(1)

# Ловим любые другие непредвиденные ошибки
except Exception as error:
    print(f"Произошла непредвиденная ошибка: {error}")
    sys.exit(1)
