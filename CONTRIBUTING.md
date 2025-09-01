# Contributing to Primes

We welcome contributions to the Primes library! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Madhulatha-Sandeep/primes.git
cd primes

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Code Style

- Follow PEP 8 Python style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Keep line length under 100 characters

## Testing

Run tests before submitting your changes:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=primes

# Run specific test file
pytest tests/test_aks.py
```

## Adding New Algorithms

When adding new primality testing algorithms:

1. Create a new module in `src/primes/`
2. Follow the same interface pattern as AKS:
   - `is_prime(n: int) -> bool`
   - `is_prime_detailed(n: int) -> Dict`
3. Add comprehensive tests in `tests/`
4. Update documentation in `docs/`
5. Add examples in `examples/`

## Documentation

- Update relevant documentation when making changes
- Add docstrings to new functions and classes
- Include mathematical background for new algorithms
- Provide usage examples

## Pull Request Process

1. Update the README.md if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update documentation
5. Create a pull request with a clear description

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a welcoming environment

## Questions?

If you have questions about contributing, please open an issue on GitHub or reach out to the maintainers.
