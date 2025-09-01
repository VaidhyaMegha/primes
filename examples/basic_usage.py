"""
Basic usage examples for the AKS primality test.
"""

from primes.aks import AKSPrimalityTest


def main():
    """Demonstrate basic usage of the AKS primality test."""
    
    # Create an instance of the AKS test
    aks = AKSPrimalityTest()
    
    # Test some numbers
    test_numbers = [2, 3, 4, 17, 25, 31, 97, 100, 101]
    
    print("=== Basic AKS Primality Test ===")
    print("Number | Is Prime?")
    print("-" * 20)
    
    for n in test_numbers:
        is_prime = aks.is_prime(n)
        print(f"{n:6d} | {is_prime}")
    
    print("\n=== Detailed Analysis for n = 31 ===")
    result = aks.is_prime_detailed(31)
    print(f"Number: {result['n']}")
    print(f"Is Prime: {result['is_prime']}")
    print(f"Algorithm: {result['algorithm']}")
    print("\nStep-by-step execution:")
    
    for step in result['steps']:
        print(f"Step {step['step']}: {step['description']} -> {step['result']}")


if __name__ == "__main__":
    main()
