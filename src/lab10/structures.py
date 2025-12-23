from typing import Any, Optional
from collections import deque

class Stack:
    """
    Структура данных «стек» (LIFO - Last In, First Out) на базе list.
    """
    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self) -> Any:
        """
        Снять верхний элемент стека и вернуть его.
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        """
        Вернуть верхний элемент без удаления.
        Возвращает None, если стек пуст.
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Вернуть True, если стек пуст, иначе False."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    """
    Структура данных «очередь» (FIFO - First In, First Out) на базе collections.deque.
    """
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Взять элемент из начала очереди и вернуть его.
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        """
        Вернуть первый элемент без удаления.
        Возвращает None, если очередь пуста.
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Вернуть True, если очередь пуста."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    print("=== Демонстрация Стека ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Стек после добавлений: длина={len(stack)}, вершина={stack.peek()}")
    print(f"Извлечено: {stack.pop()}")
    print(f"Извлечено: {stack.pop()}")
    print(f"Стек пуст? {stack.is_empty()}")
    print(f"Извлечено: {stack.pop()}")
    print(f"Стек пуст? {stack.is_empty()}")

    print("\n=== Демонстрация Очереди ===")
    queue = Queue()
    queue.enqueue("Первый")
    queue.enqueue("Второй")
    queue.enqueue("Третий")
    print(f"Очередь после добавлений: длина={len(queue)}, первый={queue.peek()}")
    print(f"Извлечено из очереди: {queue.dequeue()}")
    print(f"Извлечено из очереди: {queue.dequeue()}")
    print(f"Очередь пуста? {queue.is_empty()}")
    print(f"Извлечено из очереди: {queue.dequeue()}")
    print(f"Очередь пуста? {queue.is_empty()}")
