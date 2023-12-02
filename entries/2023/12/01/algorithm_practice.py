class Algorithm:
    def fibonacci_sequence(n):
        # Display the fibonacci sequence up to n elements
        sequence = [0, 1]

        if n <= 0:
            return sequence[0]
        elif n == 1:
            return sequence[1]

        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])

        return sequence
