from typing import Any, Optional, Iterator

class Node:
    """Узел односвязного списка."""
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список."""
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка.
        Сложность: O(1) благодаря использованию tail.
        """
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Если список не пуст, tail точно существует
            self.tail.next = new_node
            self.tail = new_node
            
        self._size += 1

    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка.
        Сложность: O(1).
        """
        new_node = Node(value, next_node=self.head)
        self.head = new_node
        
        # Если список был пуст, новый элемент является и хвостом
        if self.tail is None:
            self.tail = new_node
            
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу.
        Сложность: O(n).
        Raises:
            IndexError: Если индекс вне диапазона [0, size].
        """
        if idx < 0 or idx > self._size:
            raise IndexError("list index out of range")
            
        if idx == 0:
            self.prepend(value)
            return
            
        if idx == self._size:
            self.append(value)
            return

        # Ищем узел, после которого нужно вставить (индекс idx-1)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        # current сейчас указывает на узел (idx-1)
        new_node = Node(value, next_node=current.next)
        current.next = new_node
        
        self._size += 1

    def remove(self, value: Any) -> None:
        """
        Удалить первое вхождение значения value.
        Если элемента нет, ничего не делает (или можно выбросить ValueError).
        Сложность: O(n).
        """
        if self.head is None:
            return

        # Если удаляемый элемент в голове
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None: # Список стал пустым
                self.tail = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                # Нашли элемент для удаления (current.next)
                current.next = current.next.next
                
                # Если удалили последний элемент, нужно обновить tail
                if current.next is None:
                    self.tail = current
                
                self._size -= 1
                return
            current = current.next

    def __iter__(self) -> Iterator[Any]:
        """Возвращает итератор по значениям в списке."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"

    def __str__(self) -> str:
        """Красивый вывод: [A] -> [B] -> None"""
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


if __name__ == "__main__":
    print("=== Демонстрация Односвязного Списка ===")
    ll = SinglyLinkedList()
    
    print("1. Добавление в конец 1, 2, 3")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"Список: {ll}")
    
    print("\n2. Добавление в начало 0")
    ll.prepend(0)
    print(f"Список: {ll}")
    
    print("\n3. Вставка 1.5 по индексу 2")
    ll.insert(2, 1.5)
    print(f"Список: {ll}")
    
    print("\n4. Удаление элемента 2")
    ll.remove(2)
    print(f"Список: {ll}, Размер: {len(ll)}")
    
    print("\n5. Удаление головы (0)")
    ll.remove(0)
    print(f"Список: {ll}")
