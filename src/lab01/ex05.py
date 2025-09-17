fio = input("ФИО: ")
fio_stripped = fio.strip()
initials = "".join([word[0].upper() for word in fio_stripped.split()]) + "."
length = len(fio_stripped)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")