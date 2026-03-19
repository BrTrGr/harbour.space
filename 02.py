
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""
class User:
  def __init__(self, name):
    self.name = name
  def say_hi(self):
    print(f"Hello, I am {self.name}")

"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""
class BankAccount:
  def __init__(self, owner: str, balance: float = 0.0) -> None:
    self.owner = owner
    if balance < 0: self._balance = 0.0
    else: self._balance = balance
  def deposit(self, amount: float) -> None:
    if amount > 0: self._balance += amount
  def withdraw(self, amount: float) -> None:
    if amount > 0 and amount <= self._balance:
      self._balance -= amount
    

"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""
class Team:
  def __init__(self) -> None:
    self.members = []
  def add(self, name: str) -> None:
    self.members.append(name)
  def __len__(self) -> int:
    return len(self.members)

""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""

class QueueState:
  def __init__(self) -> None:
    self.items = []
  def push(self, item: str) -> None:
    self.items.append(item)
  def pop(self) -> str | None:
    if self.items == None:
      return None
    return self.items.pop(0)

""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""
class PaymentError(Exception):
  pass
class InsufficientFunds(PaymentError):
  pass
class Wallet:
  def __init__(self, balance: float = 0.0):
    if balance >= 0:
      self.balance = balance
    else:
        raise ValueError
  def top_up(self, amount: float):
    if amount <= 0:
      raise ValueError
    self.balance += amount
  def pay(self, amount: float):
    if amount <= 0:
      raise ValueError()
    if amount > self.balance:
      raise InsufficientFunds()
    self.balance -= amount
"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []
    def add_item(self, name: str, price: float, qty: int = 1) -> None:
        if price >= 0 and qty > 0:
            self.items.append({"name": name, "price": price, "qty": qty})
    def total_items(self) -> int:
        return sum(item["qty"] for item in self.items)
    def total_price(self) -> float:
        return sum(item["price"] * item["qty"] for item in self.items)
    def __repr__(self) -> str:
        return f"ShoppingCart(items={self.total_items()}, total={self.total_price()})"

"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""
class Classroom:
  school_name = "Harbour Space"
  def __init__(self, group_name: str):
    self.group_name = group_name
    self.students = []
  def add_student(self, name: str):
    self.students.append(name)
  def __len__(self):
    return len(self.students)
  @classmethod
  def set_school_name(cls, new_name: str):
    cls.school_name = new_name

"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""
class Rectangle:
  def __init__(self, width: float, height: float):
    self.width = abs(width)
    self.height = abs(height)
  def area(self):
    return float(self.height * self.width)
  def perimeter(self):
    return float(self.height*2 + self.width*2)

"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""
class Playlist:
  def __init__(self):
    self.songs = []
  def add(self, song: str):
    self.songs.append(song)
  def __len__(self) -> int:
    return len(self.songs)
  def __iter__(self):
    return iter(self.songs)
  def __contains__(self, song: str):
    return song in self.songs

"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""
class Product:
  def __init__(self, name: str, price: float):
    self.name = name
    self.price = price
  def get_price(self):
    return self.price
  def set_price(self, value: float):
    self.price = value
  def apply_discount(self, percent: float):
    self.price -= self.price * (percent/100)

"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""

class Person:
  def __init__(self, name=str):
    self.name = name
  def describe(self):
    return f"Person(name={self.name})"
  
class Student(Person):
  def __init__(self, name, group):
    super().__init__(name)
    self.group = group
  def describe(self, name):
    return f"Student(name={self.name}, group={self.group})"

"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""
class Point2D:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
  def distance_to(self, other: "Point2D"):
    return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
  def __eq__(self, other: object):
    return isinstance(other, Point2D) and self.x == other.x and self.y == other.y
  def __repr__(self):
    return f"Point2D({self.x}, {self.y})"
"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""
class Inventory:
  def __init__(self) -> None:
    self.inventory = {}
  def add(self, name: str, qty: int = 1) -> None:
    if qty > 0: self.inventory[name] = self.inventory.get(name, 0) + qty
  def remove(self, name: str, qty: int = 1) -> None:
    if qty > 0 and name in self.inventory:
      self.inventory[name] -= qty
      if self.inventory[name] <= 0:
        del self.inventory[name]
  def count(self, name: str) -> int:
    return self.inventory.get(name, 0)
  def __contains__(self, name: str) -> bool:
    return name in self.inventory
  def __len__(self) -> int:
    return len(self.inventory)
    
    

"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""
class CourseCatalog:
  def __init__(self) -> None:
    self._catalog: dict[str, str] = {}
  def add_course(self, code: str, title: str) -> None:
    self._catalog[code] = title
  def get_title(self, code: str) -> str | None:
    return self._catalog.get(code)
  def __iter__(self):
    return iter(sorted(self._catalog.items()))
  def __len__(self) -> int:
    return len(self._catalog)

"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""
class DefaultDict:
      def __init__(self, default_factory=None) -> None:
        self.store = {}
        if not callable(default_factory):
          self.default_factory = None
        else:
          self.default_factory = default_factory
          
      def __getitem__(self, key):
        if key in self.store:
          return self.store[key]
        if self.default_factory is None:
          return None
        value = self.default_factory()
        self.store[key] = value
        return value
      
      def __setitem__(self, key, value) -> None:
        self.store[key] = value
        
      def __contains__(self, key) -> bool:
        return key in self.store
      
      def __len__(self) -> int:
        return len(self.store)
      
      