import utils
import theorems

def main():
    try:
        n = list(map(int, input("Enter the different values of voters (n) separated by space: ").strip().split()))
        m = input("Enter 0 for simple majority; minimum threshold in % for super-majority: ")
        type = input("Enter 0 to use the deterministic approach, 1 for Monte Carlo simulation: ")
    except ValueError:
        print("Invalid input. Please enter numerical values separated by space.")
        return
    theorems.condorcet(n, type, m)

if __name__ == "__main__":
    main()