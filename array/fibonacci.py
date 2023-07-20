def fibonacci(n):
    fib_sequence = [0, 1]  

    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

num_terms = 10 
fib_sequence = fibonacci(num_terms)
print(fib_sequence)
