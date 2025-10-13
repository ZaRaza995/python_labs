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
print(normalize("ПрИвЕт\nМИр\t"))       
print(normalize("ёжик, Ёлка"))      
print(normalize("Hello\r\nWorld"))     
print(normalize( "  двойные   пробелы  "))


import re   
def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))


def count_freq_manual(tokens: list[str]) -> dict[str, int]:
    if not tokens:
        return {}
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict
print(count_freq_manual(["a","b","a","c","b","a"]))
print(count_freq_manual(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]