import utils
import theorems

def main():
    try:
        n = list(map(int, input("Enter the different values of voters (n) separated by space: ").strip().split()))
        t = input("Enter 0 to use the deterministic approach, 1 for Monte Carlo simulation: ")
    except ValueError:
        print("Invalid input. Please enter numerical values separated by space.")
        return
    t = 0
    theorems.condorcet(n, t)

if __name__ == "__main__":
    main()