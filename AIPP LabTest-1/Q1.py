def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return []

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

# --- Take input from user ---
try:
    n = int(input("Enter the number of terms: "))
    print(f"Fibonacci sequence with {n} terms:")
    print(fibonacci(n))
except ValueError as e:
    print("Error:", e)