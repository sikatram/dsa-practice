from queue_practice import Queue
from algorithm_practice import Algorithm


def main():
    data_structure_test()
    algorithm_test()
    print("\nProgram Complete")


def data_structure_test():
    print("\n-----Data Structure Test-----")
    print("\n- - -Queue- - -")
    queue = Queue()
    queue.enqueue(1)
    print("Enqueue: 1")
    print(f"Current Queue: {queue.items}")
    queue.enqueue(2)
    print("Enqueue: 2")
    print(f"Current Queue: {queue.items}")
    queue.enqueue(3)
    print("Enqueue: 3")
    print(f"Current Queue: {queue.items}")
    print(f"Queue is Empty: {queue.is_empty()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Front: {queue.front()}")
    print(f"Queue is Empty: {queue.is_empty()}")
    print(f"Current Queue: {queue.items}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Front: {queue.front()}")
    print(f"Queue is Empty: {queue.is_empty()}")
    print(f"Current Queue: {queue.items}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Front: {queue.front()}")
    print(f"Queue is Empty: {queue.is_empty()}")
    print(f"Current Queue: {queue.items}")


def algorithm_test():
    print("\n-----Algorithm Test-----")
    print("\n- - -Binary Search- - -")
    sorted_arr = [0, 1, 7, 8, 9, 10]
    target = 7
    print(f"Sorted Array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Index: {Algorithm.binary_search(sorted_arr, target)}")

    sorted_arr = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
    target = 8
    print(f"\nSorted Array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Index: {Algorithm.binary_search(sorted_arr, target)}")

    sorted_arr = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
    target = 0
    print(f"\nSorted Array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Index: {Algorithm.binary_search(sorted_arr, target)}")

    sorted_arr = [1, 2, 3, 4, 5]
    target = 5
    print(f"\nSorted Array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Index: {Algorithm.binary_search(sorted_arr, target)}")

    sorted_arr = [3]
    target = 3
    print(f"\nSorted Array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Index: {Algorithm.binary_search(sorted_arr, target)}")


if __name__ == "__main__":
    main()
