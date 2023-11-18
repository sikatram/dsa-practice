class Algorithm:
    def fibonacci_sequence(n):
        sequence = [0, 1]

        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

        return sequence
