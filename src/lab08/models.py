from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        Валидация полей после инициализации.
        """
        # Проверка на пустые строки
        if not self.fio or not self.fio.strip():
            raise ValueError("ФИО не может быть пустым.")
        if not self.group or not self.group.strip():
            raise ValueError("Группа не может быть пустой.")

        # Валидация формата даты
        try:
            b_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Неверный формат даты рождения: {self.birthdate}. Ожидается YYYY-MM-DD.")

        # Проверка, что дата рождения не в будущем
        if b_date > date.today():
             raise ValueError(f"Дата рождения не может быть в будущем: {self.birthdate}")

        # Валидация диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть от 0 до 5. Получено: {self.gpa}")

    def age(self) -> int:
        """
        Возвращает количество полных лет.
        """
        b_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
        return age

    def to_dict(self) -> dict[str, Any]:
        """
        Сериализация в словарь.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> 'Student':
        """
        Десериализация из словаря.
        """
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"])
        )

    def __str__(self) -> str:
        """
        Красивый вывод.
        """
        return f"Student(fio='{self.fio}', age={self.age()}, group='{self.group}', gpa={self.gpa})"
