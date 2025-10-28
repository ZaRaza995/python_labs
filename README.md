# python_labs

Лабораторные работы по Python

---

## ЛАБОРАТОРНАЯ РАБОТА 5

### Цель работы

Разобраться с форматами JSON, CSV и XLSX. Реализовать конвертацию между форматами.

### Код программы

- [json_csv.py](src/lab05/json_csv.py) - модуль для конвертации JSON↔CSV
- [csv_xlsx.py](src/lab05/csv_xlsx.py) - модуль для конвертации CSV→XLSX

### Входные данные

![people.csv](images/lab05/img05.png)

![people.json](images/lab05/img04.png)

![cities.csv](images/lab05/img02.png)

### Выходные файлы

![people_from_json.csv](images/lab05/img03.png)

![Excel файл](images/lab05/img01.png)

![people_from_json.xlsx](images/lab05/img06.png)

### Обработка ошибок

- Несуществующий файл → `FileNotFoundError`
- Неверное расширение файла (.txt вместо .json) → `ValueError`
- Пустой файл → `ValueError`
- Некорректный формат JSON → `ValueError`
- CSV без заголовка → `ValueError`

### Зависимости

Установка дополнительной библиотеки:

```bash
pip install -r requirements.txt
```

Требуется только `openpyxl`. Остальное - стандартная библиотека Python.

---

## ЛАБОРАТОРНАЯ РАБОТА 4

### Цель работы

Обработка текстовых файлов, работа с CSV, генерация отчетов.

### Код программы

- [io_txt_csv.py](src/lab04/io_txt_csv.py) - модуль для работы с файлами
- [text_report.py](src/lab04/text_report.py) - скрипт генерации отчетов

### Результаты выполнения

![Тест кейс 1](images/lab04/exA1.png)

![Тест кейс 2](images/lab04/exA2.png)

![Отчет](images/lab04/report.png)

---

## ЛАБОРАТОРНАЯ РАБОТА 3

### Цель работы

Работа с текстовыми данными: нормализация, токенизация, подсчет частоты слов.

### Код программы

- [text_stats.py](src/lab03/text_stats.py) - модуль для статистики текста

### Задание А

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if text is None:
        raise ValueError("Ошибка: текст не может быть None")
    if not isinstance(text, str):
        raise TypeError(f"Ошибка: ожидалась строка, получен {type(text).__name__}")
    if len(text) == 0:
        return ""
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    return ' '.join(text.split())

def tokenize(text: str) -> list[str]:
    import re
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq_manual(tokens: list[str]) -> dict[str, int]:
    if not tokens:
        return {}
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]
```

![Задание А](images/lab03/lab03exA.png)

### Задание В

Анализ текста с выводом статистики

![Задание В](images/lab03/lab03exB1.png)

Проверка обработки ошибок:

![Обработка ошибок](images/lab03/lab03exB2.png)

---

## ЛАБОРАТОРНАЯ РАБОТА 2

### Цель работы

Работа с функциями, списками, матрицами.

### Задание 1

Работа с числами: min/max, уникальные значения, развертывание матриц.

```python
def min_max(nums: list[float | int]):
  if not nums:
    raise ValueError("Список не может быть пустым")
  return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]):
  return sorted(list(set(nums)))

def flatten(mat: list[list | tuple]):
  result = []
  for row in mat:
    if not isinstance(row, (list, tuple)):
      raise TypeError("Все элементы должны быть списками или кортежами")
    for item in row:
      result.append(item)
  return result

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2 ]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print(flatten([[1, 2,], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```

![Задание 1](images/lab02/lab02ex01.png)

### Задание 2

Транспонирование матриц

```python
def is_rect(mat: list[list[float | int]]) -> bool:
    return all(len(row) == len(mat[0]) for row in mat) if mat else True

def transpose(mat: list[list[float | int]]):
    if not mat:
        return []
    if not is_rect(mat):
        raise ValueError("Матрица должна быть прямоугольной")
    return [[row[j] for row in mat] for j in range(len(mat[0]))]

print(transpose([[1, 2, 3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```

![Задание 2](images/lab02/lab02ex02.png)

### Задание 3

Форматирование записей студентов

```python
def format_record(rec: tuple[str, str, float]):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("ФИО должно быть не пустой строкой.")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("Группа должна быть не пустой строкой.")
    if not isinstance(gpa, (int, float)):
        raise ValueError("GPA должно быть числом.")
    
    name_parts = fio.split()    
    surname = name_parts[0]
    initials = "".join([part[0].upper() + "." for part in name_parts[1:]])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(( 3013013 , "ABB-01", 3.999)))
```

![Задание 3](images/lab02/lab02ex03.png)

---

## ЛАБОРАТОРНАЯ РАБОТА 1

### Цель работы

Основы Python: ввод-вывод, арифметические операции, работа со строками.

### Задание 1

Ввод имени и возраста

```python
name = input("Имя: ")
age = int(input("Возраст: "))

print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

![Задание 1](images/lab01/ex01.png)

### Задание 2

Сумма и среднее арифметическое

```python
a = float(input("Enter first number: ").replace(",", "."))
b = float(input("Enter second number: ").replace(",", "."))

s = a + b
avg = s / 2

print(f"sum={s:.2f}; avg={avg:.2f}")
```

![Задание 2](images/lab01/ex02.png)

### Задание 3

Расчет цены с учетом скидки и НДС

```python
price = float(input("Цена: "))
discount = float(input("Скидка (%): "))
vat = float(input("НДС (%): "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```

![Задание 3](images/lab01/ex03.png)

### Задание 4

Преобразование минут в формат часы:минуты

```python
min = int(input("Минуты: "))

hours = min // 60
minutes = min % 60

print(f"{hours}:{minutes:02d}")
```

![Задание 4](images/lab01/ex04.png)

### Задание 5

Работа с ФИО: извлечение инициалов и подсчет длины

```python
fio = input("ФИО: ")
fio_clean = " ".join(fio.split())
initials = "".join([word[0].upper() for word in fio_clean.split()]) + "."
length = len(fio_clean)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
```

![Задание 5](images/lab01/ex05.png)
