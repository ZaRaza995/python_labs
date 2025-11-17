import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="command")

    json2csv_parser = subparsers.add_parser("json2csv", help="JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True)
    json2csv_parser.add_argument("--out", dest="output", required=True)

    csv2json_parser = subparsers.add_parser("csv2json", help="CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True)
    csv2json_parser.add_argument("--out", dest="output", required=True)

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True)
    csv2xlsx_parser.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"Данные обновлены: {args.input} -> {args.output}")
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
        print(f"Данные обновлены: {args.input} -> {args.output}")
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f"Данные обновлены: {args.input} -> {args.output}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

