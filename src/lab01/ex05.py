fio = input("ФИО: ")
fio_clean = " ".join(fio.split())
initials = "".join([word[0].upper() for word in fio_clean.split()]) + "."
length = len(fio_clean)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")