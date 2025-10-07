def format_record(rec: tuple[str, str, float]):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("ФИО должно быть непустой строкой.")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("Группа должна быть непустой строкой.")
    if not isinstance(gpa, (int, float)):
        raise ValueError("GPA должно быть числом.")

    name_parts = fio.strip().split()    
    surname = name_parts[0]
    initials = "".join([part[0].upper() + "." for part in name_parts[1:]])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

test = (2413784, "BIVT-25" ,4.6 )
print(format_record(test))