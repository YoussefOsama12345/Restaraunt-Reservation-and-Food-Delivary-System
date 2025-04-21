"""
main_test.py

Entry point for running all unit tests in the project using pytest.
Discovers and runs all test files in the current directory and subdirectories.
"""

import pytest

if __name__ == "__main__":
    # Run all tests in files that match the pattern `test_*.py`
    pytest.main(["-v", "--tb=short", "--maxfail=3", "tests"])
