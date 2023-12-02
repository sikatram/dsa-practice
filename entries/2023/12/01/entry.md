# 📝 12/01/2023 Entry

## 📚 Topics
- [Queues](queue_practice.py)
- [Fibonacci Sequence](algorithm_practice.py)

## 💡 Insights

### General
- Consider the implementation of test cases for each data structure and algorithm to ensure comprehensive code validation and avoid potential oversights

## 🏆 Achievements

### Queue
- Successfully implemented `Queue()`

## ❌ Mistakes

### Fibonacci Sequence
- Returned the wrong base case values for `fibonacci_sequence()`
```python
# Attempt
    sequence = [0, 1]

    if n <= 0:
        return sequence[0]
    elif n == 1:
        return sequence[1]

# Solution
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
```

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
0
Number of elements: 1
1
Number of elements: 5
[0, 1, 1, 2, 3]
Number of elements: 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Program Complete
```