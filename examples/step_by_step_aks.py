"""
Step-by-step demonstration of the AKS primality test algorithm.
"""

from primes.aks import AKSPrimalityTest


def demonstrate_aks_steps(n: int):
    """
    Demonstrate the AKS algorithm step by step for a given number.
    
    Args:
        n: Number to test for primality
    """
    print(f"\n=== AKS Primality Test for n = {n} ===")
    
    aks = AKSPrimalityTest()
    result = aks.is_prime_detailed(n)
    
    print(f"Input: n = {n}")
    print(f"Final Result: {'PRIME' if result['is_prime'] else 'COMPOSITE'}")
    print(f"Algorithm: {result['algorithm']}")
    
    print("\nDetailed Step-by-Step Execution:")
    print("-" * 50)
    
    for i, step in enumerate(result['steps'], 1):
        step_num = step['step']
        description = step['description']
        step_result = step['result']
        
        print(f"{i:2d}. Step {step_num}: {description}")
        print(f"    → {step_result.upper()}")
        
        if step_result in ['prime', 'composite']:
            break
        print()
    
    return result['is_prime']


def compare_multiple_numbers():
    """Compare AKS results for multiple numbers."""
    test_numbers = [
        17,   # Small prime
        25,   # Perfect square (composite)
        31,   # Prime (example from Wikipedia)
        49,   # Perfect square (composite)
        97,   # Larger prime
        100,  # Composite with small factors
        101   # Prime
    ]
    
    print("=== Comparison of Multiple Numbers ===")
    print("Number | Result    | Type")
    print("-" * 30)
    
    aks = AKSPrimalityTest()
    for n in test_numbers:
        is_prime = aks.is_prime(n)
        result_str = "PRIME" if is_prime else "COMPOSITE"
        
        # Determine type for educational purposes
        if n == 1:
            type_str = "Neither prime nor composite"
        elif n in [4, 9, 16, 25, 36, 49, 64, 81, 100, 121]:
            type_str = "Perfect square"
        elif n > 1 and not is_prime:
            type_str = "Composite"
        else:
            type_str = "Prime"
        
        print(f"{n:6d} | {result_str:9s} | {type_str}")


def main():
    """Main demonstration function."""
    print("AKS Primality Test - Step-by-Step Demonstration")
    print("=" * 60)
    
    # Demonstrate detailed steps for specific numbers
    demonstrate_aks_steps(31)  # Example from Wikipedia
    demonstrate_aks_steps(25)  # Perfect power example
    demonstrate_aks_steps(97)  # Larger prime
    
    print("\n" + "=" * 60)
    compare_multiple_numbers()
    
    print("\n" + "=" * 60)
    print("Educational Notes:")
    print("- The AKS test is deterministic (always correct)")
    print("- It runs in polynomial time O(log^6 n)")
    print("- Step 5 (polynomial congruences) is the most computationally intensive")
    print("- For practical purposes, probabilistic tests like Miller-Rabin are faster")
    print("- AKS is theoretically significant as the first deterministic polynomial-time primality test")


if __name__ == "__main__":
    main()
