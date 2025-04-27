# Напишите класс HashTable, который реализует основные операции хеш-таблицы: insert (вставка элемента), search
#  (поиск элемента) и delete (удаление элемента)

class HashTable:
    def __init__(self, size): # создаем пустые списки
        self.size = size #
        self.table = [None]*size #

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delet(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return True
        return False

    def resize(self): # Увеличивает размер хеш-таблицы вдвое и перераспределяет все элементы.
        old_table = self.table
        old_size = self.size
        self.size = old_size * 2
        self.table = [None] * self.size

        for i in range(old_size): #  Перебирает каждый индекс старой таблицы.
            if old_table[i] is not None:
                for key, value in old_table[i]: #  Перебирает список пар ключ-значение по этому индексу (обработка коллизий).
                    self.insert(key, value) #  здесь вызываем существующий метод для повторной вставки пары ключ-значение.

# ------------
def simple_string_hash(value):
    hash_value = 0
    for char in value:
        hash_value += ord(char)  # ord() возвращает ASCII-код символа
    return hash_value
#------------
def string_hash(s): # Вычисляет хеш-значение для строки, суммируя ASCII-коды символов.
    hash_value = 0
    for char in s:
        hash_value += ord(char)
    return hash_value


class StringDictionary: # Инициализирует словарь строк с использованием хеш-таблицы.
    def __init__(self, capacity=15):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash_function(self, key): # Вычисляет хеш-значение для ключа с использованием string_hash().
        return string_hash(key) % self.capacity

    def _insert(self, key, value):
        index = self._hash_function(key) # Индекс, сгенерированный хеш-функцией, сохраняется в переменной index
        if self.table[index] is None: # Проверяет, пуста ли ячейка таблицы по рассчитанному индексу
            self.table[index] = [] # Если ячейка по индексу пуста (равна None), она инициализируется как пустой список
        for pair in self.table[index]: # Если в ячейке по индексу уже есть элементы начинается итерация по списку пар ключ-значение, хранящихся в этой ячейке.
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def resize(self): # Увеличивает размер хеш-таблицы вдвое и перераспределяет все элементы.
        old_table = self.table
        old_size = self.size
        self.size = old_size * 2
        self.table = [None] * self.size

        for i in range(old_size): #  Перебирает каждый индекс старой таблицы.
            if old_table[i] is not None:
                for key, value in old_table[i]: #  Перебирает список пар ключ-значение по этому индексу (обработка коллизий).
                    self._insert(key, value) #  здесь вызываем существующий метод для повторной вставки пары ключ-значение.

    def _get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

print("\nПример использования HashTable:")
table = HashTable(10)
table.insert('apple', 10)
table.insert('banana', 20)
print(table.get('apple'))

table.delet('apple')
print(table.get('apple'))

# Выводим размер таблицы до изменения размера
print(f"Размер таблицы до изменения размера: {table.size}")
table.resize()
# Выводим размер таблицы после изменения размера
print(f"Размер таблицы после изменения размера: {table.size}")

print("\nПример использования simple_string_hash:")
# Напишите функцию, которая принимает строку и возвращает её хеш-значение. Для этого используйте простой алгоритм:
# сложение ASCII-кодов всех символов строки
print('Сумма ASCII-кодов всех символов строки', simple_string_hash('apple'))

# Пример использования StringDictionary
print("\nПример использования StringDictionary:")
sd = StringDictionary()
sd._insert("one", 1)
sd._insert("two", 2)
sd._insert("three", 3)


print("Поиск 'two':", sd._get("two"))  # Вывод: 2
print("Поиск 'four':", sd._get("four"))  # Вывод: None