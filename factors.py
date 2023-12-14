import sys

def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return f"{n}={i}*{n//i}"
    return f"{n}=1*{n}"

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                num = int(line.strip())
                print(factorize(num))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print(f"Error: Invalid input in file '{file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
