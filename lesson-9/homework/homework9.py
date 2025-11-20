# ===============================

import math
from datetime import date

# -------------------------------
# 1. Circle Class
# -------------------------------
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# -------------------------------
# 2. Person Class
# -------------------------------
class Person:
    def __init__(self, name: str, country: str, birth_year: int):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year


# -------------------------------
# 3. Calculator Class
# -------------------------------
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# -------------------------------
# 4. Shape and Subclasses
# -------------------------------
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# -------------------------------
# 5. Binary Search Tree Class
# -------------------------------
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BSTNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BSTNode(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


# -------------------------------
# 6 & 9. Stack Data Structure
# -------------------------------
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

    def display(self):
        return self.stack[::-1]  # Top of stack first


# -------------------------------
# 7. Linked List Data Structure
# -------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


# -------------------------------
# 8. Shopping Cart Class
# -------------------------------
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] -= quantity
            if self.items[name]['quantity'] <= 0:
                del self.items[name]

    def total_price(self):
        return sum(v['price']*v['quantity'] for v in self.items.values())


# -------------------------------
# 10. Queue Data Structure
# -------------------------------
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        return self.queue.copy()


# -------------------------------
# 11. Bank Class
# -------------------------------
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.balance
        return "Account not found"

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        return "Account not found"

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        return "Account not found"


# -------------------------------
# Dictionary for Telegram Bot Access
# -------------------------------
TASKS = {
    "Circle": Circle,
    "Person": Person,
    "Calculator": Calculator,
    "Shape": Shape,
    "Square": Square,
    "Triangle": Triangle,
    "CircleShape": CircleShape,
    "BST": BST,
    "Stack": Stack,
    "Node": Node,
    "LinkedList": LinkedList,
    "ShoppingCart": ShoppingCart,
    "Queue": Queue,
    "BankAccount": BankAccount,
    "Bank": Bank
}
