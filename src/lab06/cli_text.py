import argparse
import sys
from pathlib import Path

# Добавляем путь к src для импорта модулей
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from lib.text import normalize, tokenize, count_freq_manual, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "cat":
        file_path = Path(args.input)
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for num, line in enumerate(file, start=1):
                    if args.n:
                        print(f"{num}: {line}", end="")
                    else:
                        print(line, end="")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    elif args.command == "stats":
        if args.top < 1:
            raise ValueError("--top должен быть > 0")

        file_path = Path(args.input)
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            normalized_text = normalize(text)
            tokens = tokenize(normalized_text)
            freq = count_freq_manual(tokens)
            top_words = top_n(freq, args.top)

            print(f"Всего слов: {len(tokens)}")
            print(f"Уникальных слов: {len(freq)}")
            print(f"Топ-{args.top}:")
            for word, count in top_words:
                print(f"{word}: {count}")
        except Exception as e:
            print(f"Ошибка при обработке файла: {e}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
