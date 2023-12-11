import utils
from theorems import condorcet

def main():
    try:
        n = list(map(int, input("Enter the different values of voters (n) separated by space: ").strip().split()))
        m = int(input("Enter 0 for simple majority; minimum threshold in % for super-majority: "))
        type = int(input("Enter 0 to use the deterministic approach, 1 for Monte Carlo simulation: "))
    except ValueError:
        print("Invalid input. Please enter numerical values separated by space.")
        return
    condorcet.plot(n, type, m)

if __name__ == "__main__":
    main()