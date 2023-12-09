import theorems

def main():
    try:
        n = list(map(int, input("Enter the different values of voters (n) separated by space: ").strip().split()))
    except ValueError:
        print("Invalid input. Please enter numerical values separated by space.")
        return

    theorems.condorcet(n)

if __name__ == "__main__":
    main()
