# Лабораторная работа №8: ООП, dataclasses и сериализация

## Описание
В данной лабораторной работе реализована модель студента с использованием декоратора `@dataclass`, методы для работы с данными (вычисление возраста) и сериализация/десериализация в формат JSON.

## Структура
- `models.py`: Содержит класс `Student` с полями `fio`, `birthdate`, `group`, `gpa`. Реализована валидация данных и методы `age()`, `to_dict()`, `from_dict()`.
- `serialize.py`: Содержит функции `students_to_json()` и `students_from_json()` для сохранения и загрузки списка студентов.

## Примеры использования

### Создание студента
```python
from src.lab08.models import Student

student = Student(
    fio="Иванов Иван",
    birthdate="2000-01-01",
    group="SE-01",
    gpa=4.5
)
print(student.age())  # Выведет возраст
```

### Сериализация
```python
from src.lab08.serialize import students_to_json

students = [student]
students_to_json(students, "students.json")
```

## Результаты
Скрипт проверки `verify.py` демонстрирует корректную работу всех методов, включая валидацию некорректных данных (неверный формат даты, выход GPA за границы).
