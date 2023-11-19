# 📝 11/19/2023 Entry

## 📚 Topics
- [Queues](queue_practice.py)
- [Fibonacci Sequence](algorithm_practice.py)

## 💡 Insights

### Fibonacci Sequence
- Consider different approaches to conditional logic and maintain proper code spacing for enhanced readability and consistency
```python
# Attempt
    if n <= 0:
        return []

    if n == 1:
        return [0]

# Solution
    if n <= 0:
        return []
    elif n == 1:
        return [0]
```

## 🏆 Achievements

### Queue
- Successfully implemented `Queue()`

### Fibonacci Sequence
- Successfully implemented `fibonacci_sequence()`

## ❌ Mistakes
- N/A

## 🖨️ Console Log
```
-----Data Structure Test-----

- - -Queue- - -
Enqueue: 1
Current Queue: [1]
Enqueue: 2
Current Queue: [1, 2]
Enqueue: 3
Current Queue: [1, 2, 3]
Queue is Empty: False
Dequeue: 1
Front: 2
Queue is Empty: False
Current Queue: [2, 3]
Dequeue: 2
Front: 3
Queue is Empty: False
Current Queue: [3]
Dequeue: 3
Front: None
Queue is Empty: True
Current Queue: []

-----Algorithm Test-----

- - -Fibonacci Sequence- - -
Number of elements: 0
[]
Number of elements: 1
[0]
Number of elements: 5
[0, 1, 1, 2, 3]
Number of elements: 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Program Complete
```