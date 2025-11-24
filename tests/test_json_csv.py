import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Алиса", "age": 22},
        {"name": "Боб", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    # CSV-ридер читает все как строки
    assert rows[0]["name"] == "Алиса"
    assert rows[0]["age"] == "22"


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "data.csv"
    dst = tmp_path / "data.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "value"])
        writer.writeheader()
        writer.writerow({"id": "1", "value": "test"})

    csv_to_json(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0] == {"id": "1", "value": "test"}


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("non_existent.json", "out.csv")


def test_json_to_csv_invalid_json(tmp_path):
    src = tmp_path / "broken.json"
    src.write_text("{broken json", encoding="utf-8")
    dst = tmp_path / "out.csv"

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path):
    src = tmp_path / "empty.csv"
    src.touch()
    dst = tmp_path / "out.json"

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))
