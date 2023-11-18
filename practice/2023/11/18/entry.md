# 📝 11/18/2023 Entry

## 📚 Topics
- [Queues](queue_practice.py)
- [Binary Search](algorithm_practice.py)

## 💡 Insights

### Binary Search
- Simplify variable assignments for readability and conciseness
```python
# Attempt
    left = 0
    right = len(sorted_arr)

# Solution
    left, right = 0, len(sorted_arr) - 1
```

- Consider optimizing the calculation of `mid` to improve the binary search algorithm's efficiency
```python
# Attempt
    mid = (left + right) // 2

# Solution
    mid = left + (right - left) // 2
```

- Pay attention to loop conditions and spacing for enhanced readability
```python
# Attempt
    while left < right:
        mid = (left + right) // 2
        if target == sorted_arr[mid]:
            return True
        elif target < sorted_arr[mid]:
            right = mid
        else:
            left = mid + 1

# Solution
    while left <= right:
        mid = left + (right - left) // 2

        if sorted_arr[mid] == target:
            # If the middle element is the target, return its index
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```

## 🏆 Achievements

### Queue
- Successfully implemented `Queue()`
- Streamlined logic in `Queue()` methods through internal method utilization

```python
# Attempt
    def front(self):
        # Return front item without removal, if not empty
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Check if the queue is empty
        return self.size() == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

# Solution
    def front(self):
        # Return front item without removal, if not empty
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
```

### Binary Search
- Implemented a functionally correct binary search algorithm

## ❌ Mistakes

### Binary Search
- Returned boolean values instead of `index`

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

- - -Binary Search- - -
Sorted Array: [0, 1, 7, 8, 9, 10]
Target: 7
Exists: True

Sorted Array: [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
Target: 8
Exists: False

Sorted Array: [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
Target: 0
Exists: True

Sorted Array: [1, 2, 3, 4, 5]
Target: 5
Exists: True

Sorted Array: [3]
Target: 3
Exists: True

Program Complete
```