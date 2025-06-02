import time

def print_matrix_versions(original, gaussed):
    def draw_matrix(matrix, title, format_str):
        if not matrix:
            print(f"{title}\n[empty]")
            return
        num_cols = len(matrix[0])
        cell_width = 12
        total_width = num_cols * cell_width + (num_cols - 1) + 2
        print(f"\n{title}")
        print("+" + "-" * (total_width - 2) + "+")
        for row in matrix:
            line = " | ".join([format_str.format(x) for x in row])
            print(f"| {line} |")
        print("+" + "-" * (total_width - 2) + "+")

    draw_matrix(original, "ORIGINAL MATRIX", "{:>10.2f}")
    draw_matrix(gaussed, "AFTER GAUSS FULL VALUES", "{:>20}")
    draw_matrix(gaussed, "AFTER GAUSS ROUNDED(2)", "{:>10.2f}")

def validate_matrix_input(prompt1):
    while True:
        try:
            N = int(input(prompt1))
            A = [list(map(int, input(f"Enter matrix`s row {i+1} space-divided: ").split())) for i in range(N)]
            if all(len(row) ==  len(A[0]) for row in A) and len(A[0]) > len(A):
                print("\nMatrix build successfully!")
                return A
            else:
                print(f"All rows must contain same number of columns -> {N+1}")
                continue
        except ValueError:
            print("Invalid input")

def gauss_elimination(matrix):
    start = time.time()
    for i in range(len(matrix)-1):
        pivot = matrix[i][i]
        if abs(pivot) < 1e-10:
            for j in range(i+1, len(matrix)):
                if abs(matrix[j][i]) > 1e-10:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            pivot = matrix[i][i]
            if abs(pivot) < 1e-10:
                continue
        for j in range(i+1, len(matrix)):
            factor = matrix[j][i] / pivot
            for k in range(i, len(matrix[i])):
                matrix[j][k] -= factor * matrix[i][k]
    end = time.time()
    print(f"\nGauss elimination took {end-start} seconds")
    return matrix

def compute_solutions(matrix):
    rank=0
    start = time.time()
    for row in matrix:
        if all(abs(x) < 1e-10 for x in row[:-1]) and abs(row[-1]) >= 1e-10:
            end = time.time()
            print(f"Matrix computed in: {end-start}")
            return 0
        if abs(sum(row[:-1])) > 1e-10:
            rank += 1
    if rank < len(matrix[0])-1:
        end = time.time()
        print(f"Matrix computed in: {end - start}")
        return float("inf")
    elif rank == len(matrix[0])-1:
        end = time.time()
        print(f"Matrix computed in: {end - start}")
        return 1

def generate_matrix():
    import random
    start = time.time()
    n = int(input("Enter number of equations (rows): "))
    m = n + 1
    print(f"\nAutomatically setting number of columns to {m} (for {n} variables and 1 column of constants).")
    min_val = float(input("\nMinimum value: "))
    max_val = float(input("Maximum value: "))
    if min_val > max_val:
        min_val,max_val = max_val,min_val
    print("\nMinimum value must be greater than maximum value. I`m swapping min and max for You...")
    matrix = [[round(random.uniform(min_val, max_val),2) for _ in range(m)] for _ in range(n)]
    print("\nMatrix generated successfully!")
    end = time.time()
    print(f"\nMatrix generated in: {end - start}")
    return matrix

def main_menu():
    commands = {
        "1": {"desc": "Enter matrix manually","action": lambda: validate_matrix_input("Enter number of rows: ")
        },
        "2": {"desc": "Generate random matrix","action": generate_matrix
        },
        "0": {"desc": "Exit","action": lambda: None}
    }
    print("\nLinear System Solver")
    print("====================")
    for key in commands:
        print(f"[{key}] {commands[key]['desc']}")

    while True:
        cmd = input("\nSelect option: ").strip()
        if cmd not in commands:
            print("Invalid choice.")
            continue
        if cmd == "0":
            print("Exiting.")
            return
        A = commands[cmd]["action"]()
        if A is None:
            print("No matrix loaded.")
            continue

        A_gaussed = gauss_elimination([row[:] for row in A])
        print_matrix_versions(A, A_gaussed)

        result = compute_solutions(A_gaussed)
        print("\nResult:")
        if result == 0:
            print("Inconsistent system (no solutions).")
        elif result == 1:
            print("Consistent system with a unique solution.")
        elif result == float("inf"):
            print("System with infinitely many solutions.")
        else:
            print("Unexpected result.")
        break

def main():

    main_menu()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"\nExecution took {end - start} seconds.")