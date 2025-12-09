import csv
from pathlib import Path
from typing import List, Dict, Any
from src.lab08.models import Student

class Group:
    
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self) -> List[Student]:
        students = []
        if not self.path.exists():
            return students
        
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student = Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"])
                    )
                    students.append(student)
                except (ValueError, KeyError):
                    # Пропускаем некорректные строки
                    continue
        return students

    def _save_all(self, students: List[Student]):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

    def list(self) -> List[Student]:
        return self._read_all()

    def add(self, student: Student):
        students = self._read_all()
        students.append(student)
        self._save_all(students)

    def find(self, substr: str) -> List[Student]:
        students = self._read_all()
        return [s for s in students if substr.lower() in s.fio.lower()]

    def remove(self, fio: str):
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        self._save_all(students)

    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False
        for student in students:
            if student.fio == fio:
                if "fio" in fields:
                    student.fio = fields["fio"]
                if "birthdate" in fields:
                    student.birthdate = fields["birthdate"]
                if "group" in fields:
                    student.group = fields["group"]
                if "gpa" in fields:
                    student.gpa = float(fields["gpa"])
                
                # Повторная валидация (простой вызов post_init)
                student.__post_init__()
                updated = True
                break 
        
        if updated:
            self._save_all(students)

    def stats(self) -> Dict[str, Any]:
        students = self._read_all()
        if not students:
            return {
                "count": 0,
                "min_gpa": 0.0,
                "max_gpa": 0.0,
                "avg_gpa": 0.0,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [s.gpa for s in students]
        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5_students": top_5
        }

if __name__ == "__main__":
    import sys
    import os
    # Хак для путей, чтобы видеть пакет src
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    from src.lab08.models import Student

    file_path = "src/data/lab09/students.csv"
    group = Group(file_path)
    
    # Простое интерактивное меню
    while True:
        print("\n--- Меню ---")
        print("1. Список студентов (List)")
        print("2. Добавить студента (Add)")
        print("3. Найти (Find)")
        print("4. Удалить (Remove)")
        print("5. Обновить (Update)")
        print("6. Статистика (Stats)")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("\nСписок студентов:")
            for s in group.list():
                print(s)
                
        elif choice == "2":
            fio = input("ФИО: ")
            bdate = input("Дата рождения (YYYY-MM-DD): ")
            grp = input("Группа: ")
            try:
                gpa = float(input("Средний балл: "))
                new_student = Student(fio, bdate, grp, gpa)
                group.add(new_student)
                print("Студент добавлен.")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
                
        elif choice == "3":
            substr = input("Введите часть ФИО для поиска: ")
            found = group.find(substr)
            if found:
                for s in found:
                    print(s)
            else:
                print("Ничего не найдено.")
                
        elif choice == "4":
            fio = input("Введите точное ФИО для удаления: ")
            group.remove(fio)
            print("Операция удаления завершена.")
            
        elif choice == "5":
            fio = input("Введите ФИО студента для обновления: ")
            found = group.find(fio)
            if not found:
                print("Студент не найден.")
                continue
            
            print("Оставьте поле пустым, если не хотите его менять.")
            new_fio = input("Новое ФИО: ")
            new_bdate = input("Новая дата рождения: ")
            new_grp = input("Новая группа: ")
            new_gpa_str = input("Новый средний балл: ")
            
            updates = {}
            if new_fio: updates["fio"] = new_fio
            if new_bdate: updates["birthdate"] = new_bdate
            if new_grp: updates["group"] = new_grp
            if new_gpa_str: 
                try:
                    updates["gpa"] = float(new_gpa_str)
                except ValueError:
                    print("Ошибка: балл должен быть числом")
                    continue
            
            try:
                group.update(fio, **updates)
                print("Данные студента обновлены.")
            except ValueError as e:
                print(f"Ошибка валидации: {e}")
                
        elif choice == "6":
            import pprint
            pprint.pprint(group.stats())
            
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
