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
    print("\n- - -Fibonacci Sequence- - -")
    n = 0
    print(f"Number of elements: {n}")
    print(Algorithm.fibonacci_sequence(n))
    n = 1
    print(f"Number of elements: {n}")
    print(Algorithm.fibonacci_sequence(n))
    n = 5
    print(f"Number of elements: {n}")
    print(Algorithm.fibonacci_sequence(n))
    n = 10
    print(f"Number of elements: {n}")
    print(Algorithm.fibonacci_sequence(n))


if __name__ == "__main__":
    main()
