def fibonacci(input_number):
    fib_sequence = [0, 1]

    while len(fib_sequence) < input_number:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
 
    return fib_sequence


input_number = 5
fib_numbers = fibonacci(input_number)
print(fib_numbers)
