# 📝 11/16/2023 Entry

## 📚 Topics
- [Stacks](stack_practice.py)

## 💡 Insights

### Stack
- Utilize internal methods for streamlined logic execution
```python

# Attempt
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if self.items:
            return self.items.pop()
        else:
            return "Stack is Empty"

# Solution
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()
```
- Explore different logical constructs for efficiency and readability
```python
# Attempt
    def is_empty(self):
        # Check if the stack is empty
        if self.items:
            return True
        else:
            return False
# Solution
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
```

## 🏆 Achievements
### Stack
- Successfully implemented methods `__init__`, `push`, `peek`, `is_empty`, and `size`

## ❌ Mistakes
### Stack

- Logical inversion in `is_empty` method
```python
# Attempt
    def is_empty(self):
        # Check if the stack is empty
        if self.items:
            return True
        else:
            return False

# Solution
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
```
- `pop()` method should return `None` for an empty stack instead of a string
```python
# Attempt
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if self.items:
            return self.items.pop()
        else:
            return "Stack is Empty"

# Solution
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()
```

## 🖨️ Console Log
```
-----Data Structure Test-----

- - -Stack- - -
Push: 1
Current Stack: [1]
Push: 2
Current Stack: [1, 2]
Push: 3
Current Stack: [1, 2, 3]
Stack is Empty: True
Pop: 3
Peek: 2
Stack is Empty: True
Current Stack: [1, 2]
Pop: 2
Peek: 1
Stack is Empty: True
Current Stack: [1]
Pop: 1
Peek: None
Stack is Empty: False
Current Stack: []

Program Complete
```