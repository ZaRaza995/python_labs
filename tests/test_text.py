import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# --- Тесты для normalize ---
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


# --- Тесты для tokenize ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("привет, мир!", ["привет", "мир"]),
        ("раз-два три", ["раз-два", "три"]),
        ("", []),
        ("   ", []),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


# --- Тесты для count_freq ---
def test_count_freq_basic():
    tokens = ["яблоко", "банан", "яблоко", "апельсин", "банан", "яблоко"]
    expected = {"яблоко": 3, "банан": 2, "апельсин": 1}
    assert count_freq(tokens) == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


# --- Тесты для top_n ---
def test_top_n_basic():
    freq = {"яблоко": 3, "банан": 2, "апельсин": 1, "виноград": 4}
    # виноград: 4, яблоко: 3, банан: 2, апельсин: 1
    expected = [("виноград", 4), ("яблоко", 3), ("банан", 2), ("апельсин", 1)]
    assert top_n(freq, n=4) == expected


def test_top_n_limit():
    freq = {"a": 10, "b": 5, "c": 1}
    assert top_n(freq, n=2) == [("a", 10), ("b", 5)]


def test_top_n_tie_breaker():
    # Если частоты равны, сортировка должна быть алфавитной
    freq = {"b": 5, "a": 5}
    expected = [("a", 5), ("b", 5)]
    assert top_n(freq, n=2) == expected
