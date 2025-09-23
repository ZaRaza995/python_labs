from typing import List, Optional

def build_roster(names: List[Optional[str]], extra: List[str] = None):
    if extra is None:
        extra = []
    
    processed_names = []
    for name in names:
        if name is not None:
            processed_names.append(name.strip().title())
    
    for name in extra:
        if name is not None:
            processed_names.append(name.strip().title())
    
    return processed_names

def main():  
    students = ["\t  анНА  ", "  ", "", None, "пЁТР"]
    extra = []
    roster = build_roster(students, extra)
    print("Результат roster:", roster) 

if __name__ == "__main__":
    main()