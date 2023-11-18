# 📝 11/17/2023 Entry

## 📚 Topics
- [Stacks](stack_practice.py)
- [Fibonacci Sequence](algorithm_practice.py)

## 💡 Insights

### Fibonacci Sequence
- Identified a limitation in `fibonacci_sequence_solution.py`: it does not handle cases where `n` is 1 or less effectively

## 🏆 Achievements
### Stack
- Successfully implemented `Stack()` and `fibonacci_sequence()`
- Utilized internal methods for streamlined logic execution
```python
# Attempt
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()

# Solution
    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()
```
- Explored different logical constructs for efficiency and readability
```python
# Attempt
    def is_empty(self):
        # Check if the stack is empty
        return self.size() == 0

# Solution
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
```

## ❌ Mistakes
### General
- Need to focus on consistent Python formatting standards, particularly regarding indentation and spacing

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
Stack is Empty: False
Pop: 3
Peek: 2
Stack is Empty: False
Current Stack: [1, 2]
Pop: 2
Peek: 1
Stack is Empty: False
Current Stack: [1]
Pop: 1
Peek: None
Stack is Empty: True
Current Stack: []

-----Algorithm Test-----

- - -Fibonacci Sequence- - -
Number of elements: 15
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

Program Complete
```