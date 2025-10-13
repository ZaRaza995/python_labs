import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lib.text import *


input_text = sys.stdin.readline()
normalized_text = normalize(input_text)
tokens = tokenize(normalized_text)

frequencies = count_freq_manual(tokens)
top_5_words = top_n(frequencies, n=5)

if not tokens:
        raise ValueError("строка не должна быть пустой или содержать только пробелы.")

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(frequencies)}")
print("Топ-5:")
for word, freq in top_5_words:
    print(f"{word}:{freq}")