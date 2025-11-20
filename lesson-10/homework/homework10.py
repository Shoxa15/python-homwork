
from datetime import date, datetime

# ===============================
# HOMEWORK 1: ToDo List Application
# ===============================

class Task:
    def __init__(self, title, description='', due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date  # Should be a datetime.date object
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        due = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"Task(title='{self.title}', status={status}, due={due})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def list_all_tasks(self):
        return self.tasks

    def incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

# Example Usage
# todo = ToDoList()
# todo.add_task(Task("Learn Python", "Practice OOP", datetime(2025,11,25).date()))
# todo.add_task(Task("Buy groceries"))
# print(todo.list_all_tasks())
# print(todo.incomplete_tasks())


# ===============================
# HOMEWORK 2: Simple Blog System
# ===============================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()

    def __repr__(self):
        return f"Post(title='{self.title}', author='{self.author}', date='{self.date.strftime('%Y-%m-%d %H:%M:%S')}')"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts

    def posts_by_author(self, author_name):
        return [p for p in self.posts if p.author == author_name]

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content
                return True
        return False

    def latest_posts(self, n=5):
        return sorted(self.posts, key=lambda x: x.date, reverse=True)[:n]

# Example Usage
# blog = Blog()
# blog.add_post(Post("My First Post", "Content here", "Alice"))
# blog.add_post(Post("Python Tips", "Use OOP", "Bob"))
# print(blog.list_posts())
# print(blog.posts_by_author("Alice"))


# ===============================
# HOMEWORK 3: Simple Banking System
# ===============================

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"Account({self.account_number}, Holder={self.holder_name}, Balance={self.balance})"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        self.accounts[account.account_number] = account

    def get_balance(self, account_number):
        acc = self.accounts.get(account_number)
        if acc:
            return acc.balance
        return "Account not found"

    def deposit(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            return acc.deposit(amount)
        return "Account not found"

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            return acc.withdraw(amount)
        return "Account not found"

    def transfer(self, from_acc_number, to_acc_number, amount):
        from_acc = self.accounts.get(from_acc_number)
        to_acc = self.accounts.get(to_acc_number)
        if not from_acc or not to_acc:
            return "Account not found"
        if from_acc.balance < amount:
            return "Insufficient funds"
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        return True

    def account_details(self, account_number):
        acc = self.accounts.get(account_number)
        if acc:
            return acc
        return "Account not found"

# Example Usage
# bank = Bank()
# acc1 = Account("001", "Alice", 1000)
# acc2 = Account("002", "Bob", 500)
# bank.add_account(acc1)
# bank.add_account(acc2)
# print(bank.get_balance("001"))
# bank.transfer("001", "002", 200)
# print(bank.account_details("001"))
# print(bank.account_details("002"))


# ===============================
# Dictionary for Telegram Bot Access
# ===============================
TASKS = {
    "Task": Task,
    "ToDoList": ToDoList,
    "Post": Post,
    "Blog": Blog,
    "Account": Account,
    "Bank": Bank
}
