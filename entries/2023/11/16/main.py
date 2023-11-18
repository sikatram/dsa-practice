from stack_practice import Stack


def main():
    data_structure_test()
    print("\nProgram Complete")


def data_structure_test():
    print("\n-----Data Structure Test-----")
    print("\n- - -Stack- - -")
    stack = Stack()
    stack.push(1)
    print("Push: 1")
    print(f"Current Stack: {stack.items}")
    stack.push(2)
    print("Push: 2")
    print(f"Current Stack: {stack.items}")
    stack.push(3)
    print("Push: 3")
    print(f"Current Stack: {stack.items}")
    print(f"Stack is Empty: {stack.is_empty()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Stack is Empty: {stack.is_empty()}")
    print(f"Current Stack: {stack.items}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Stack is Empty: {stack.is_empty()}")
    print(f"Current Stack: {stack.items}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Stack is Empty: {stack.is_empty()}")
    print(f"Current Stack: {stack.items}")


if __name__ == "__main__":
    main()
