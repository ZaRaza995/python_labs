# python_labs
## Лабораторная работа 1

### 1 задание

```name = input("Имя: ")
age = int(input("Возраст: "))

print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![alt text](images/lab01/ex01.png)

### 2 задание

```a = float(input("Enter first number: ").replace(",", "."))
b = float(input("Enter second number: ").replace(",", "."))

s = a + b
avg = s / 2

print(f"sum={s:.2f}; avg={avg:.2f}")
```
![alt text](images/lab01/ex02.png)

### 3 задание

```price = float(input("Цена: "))
discount = float(input("Скидка (%): "))
vat = float(input("НДС (%): "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```
![alt text](images/lab01/ex03.png)

### 4 задание

```min = int(input("Минуты: "))

hours = min // 60
minutes = min % 60

print(f"{hours}:{minutes:02d}")
```
![alt text](images/lab01/ex04.png)


### 5 задание

```fio = input("ФИО: ")
fio_stripped = fio.strip()
initials = "".join([word[0].upper() for word in fio_stripped.split()]) + "."
length = len(fio_stripped)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
```

![alt text](images/lab01/ex05.png)
