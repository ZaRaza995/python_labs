import json
from typing import List
from src.lab08.models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.
    """
    # Сортируем студентов по убыванию среднего балла (GPA)
    students.sort(key=lambda s: s.gpa, reverse=True)
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    """
    Читает JSON файл и возвращает список студентов.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
