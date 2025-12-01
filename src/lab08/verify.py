from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json
import os

def verify():
    print("=== Начало проверки ===")

    # 1. Тестирование создания и валидации студента
    print("\n1. Тестирование создания и валидации студента...")
    try:
        s1 = Student("Тестовый Пользователь", "2000-01-01", "G1", 4.5)
        print(f"Создан: {s1}")
        print(f"Возраст: {s1.age()}")
    except Exception as e:
        print(f"Не удалось создать корректного студента: {e}")

    # Тест неверной даты
    try:
        Student("Неверная Дата", "2000/01/01", "G1", 4.5)
        print("Ошибка: Неверный формат даты НЕ пойман")
    except ValueError as e:
        print(f"Поймана ожидаемая ошибка (дата): {e}")

    # Тест неверного среднего балла
    try:
        Student("Неверный GPA", "2000-01-01", "G1", 11.0)
        print("Ошибка: Неверный GPA НЕ пойман")
    except ValueError as e:
        print(f"Поймана ожидаемая ошибка (GPA): {e}")

    # Тест пустого имени
    try:
        Student("", "2000-01-01", "G1", 4.5)
        print("Ошибка: Пустое имя НЕ поймано")
    except ValueError as e:
        print(f"Поймана ожидаемая ошибка (имя): {e}")

    # Тест даты из будущего
    try:
        Student("Марти Макфлай", "2077-01-01", "G1", 4.5)
        print("Ошибка: Дата из будущего НЕ поймана")
    except ValueError as e:
        print(f"Поймана ожидаемая ошибка (будущее): {e}")

    # 2. Тестирование сериализации
    print("\n2. Тестирование сериализации...")
    input_path = "src/data/lab08/students_input.json"
    output_path = "src/data/lab08/students_output.json"
    
    # Убедимся, что входной файл существует
    if not os.path.exists(input_path):
        print(f"Ошибка: {input_path} не найден")
        return

    students = students_from_json(input_path)
    print(f"Загружено {len(students)} студентов из {input_path}")
    for s in students:
        print(f" - {s}")

    print(f"Сохранение в {output_path}...")
    students_to_json(students, output_path)
    
    if os.path.exists(output_path):
        print("Выходной файл успешно создан.")
        # Проверка соответствия содержимого
        students_reloaded = students_from_json(output_path)
        print(f"Перезагружено {len(students_reloaded)} студентов из выходного файла.")
        
        # Проверяем количество (порядок может измениться из-за сортировки)
        assert len(students) == len(students_reloaded)
        
        # Проверяем, что первый студент имеет самый высокий балл
        if len(students_reloaded) > 0:
            top_student = students_reloaded[0]
            print(f"Лучший студент: {top_student.fio} (GPA: {top_student.gpa})")
            
        print("Проверка пройдена!")
    else:
        print("Ошибка: Выходной файл не создан.")

    print("\n=== Конец проверки ===")

if __name__ == "__main__":
    verify()
