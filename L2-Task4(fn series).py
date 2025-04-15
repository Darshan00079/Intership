def generate_fn_sequence(n):
    if n <= 0:
        return "Please enter a positive integer."
    fibonnaci_seq=[0,1]
    for _ in range(2,n):
        next_term = fibonnaci_seq[-1] + fibonnaci_seq[-2]
        fibonnaci_seq.append(next_term)
    return fibonnaci_seq[:n]

terms=int(input("Enter the number of terms: "))

print("Fibonnaci sequence =", generate_fn_sequence(terms))
