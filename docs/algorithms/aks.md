# AKS Primality Test

## Overview

The AKS primality test, developed by Manindra Agrawal, Neeraj Kayal, and Nitin Saxena in 2002, is the first deterministic polynomial-time algorithm for testing primality. This breakthrough result proved that the PRIMES problem is in complexity class P.

## Algorithm Description

The AKS test is based on the following generalization of Fermat's Little Theorem:

> A number n > 1 is prime if and only if the polynomial congruence
> (x + a)ⁿ ≡ xⁿ + a (mod n)
> holds for all integers a coprime to n.

However, checking all such a would take exponential time. The key insight of AKS is that it suffices to check this congruence modulo (xʳ - 1) for an appropriately chosen r, and only for a limited number of values of a.

## Algorithm Steps

1. **Perfect Power Check**: If n = aᵇ for integers a > 1 and b > 1, output COMPOSITE.

2. **Find Suitable r**: Find the smallest r such that ordᵣ(n) > (log₂ n)².

3. **GCD Check**: If gcd(a,n) > 1 for some a ≤ r, output COMPOSITE.

4. **Small n Check**: If n ≤ r, output PRIME.

5. **Polynomial Congruence Check**: For a = 1 to ⌊√φ(r) log₂(n)⌋, check if:
   (x + a)ⁿ ≡ xⁿ + a (mod xʳ - 1, n)
   If any check fails, output COMPOSITE.

6. **Output PRIME**: If all checks pass, output PRIME.

## Complexity Analysis

- **Time Complexity**: O(log⁶ n) in the original version
- **Space Complexity**: O(log³ n)
- **Deterministic**: Yes (always gives correct answer)

## Implementation Notes

### Key Components

1. **Mathematical Utilities**: GCD, modular exponentiation, Euler's totient function
2. **Polynomial Arithmetic**: Operations in Z[x]/(xʳ-1,n)
3. **Perfect Power Detection**: Efficient algorithm to detect if n = aᵇ

### Optimizations

The implementation includes several optimizations:
- Efficient polynomial modular exponentiation
- Optimized perfect power detection
- Early termination conditions

## Example Execution

For n = 31:

1. **Step 1**: 31 is not a perfect power ✓
2. **Step 2**: Find r = 29 such that ord₂₉(31) > (log₂ 31)² = 25 ✓
3. **Step 3**: No integer in [2, 29] divides 31 ✓
4. **Step 4**: 31 > 29, continue ✓
5. **Step 5**: Check polynomial congruences for a = 1 to 26
   - All congruences (x + a)³¹ ≡ x³¹ + a (mod x²⁹ - 1, 31) hold ✓
6. **Step 6**: Output PRIME ✓

## References

1. Agrawal, M., Kayal, N., & Saxena, N. (2004). PRIMES is in P. Annals of Mathematics, 160(2), 781-793.
2. [Original Paper PDF](https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf)
3. [Wikipedia Article](https://en.wikipedia.org/wiki/AKS_primality_test)
