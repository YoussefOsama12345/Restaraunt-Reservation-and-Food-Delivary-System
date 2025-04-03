"""
- **Flake8 - Style Guide Checker**
- Enforces PEP 8 coding style guidelines.
- Checks for indentation issues, unused imports, and line length violations.
- Improves code readability and maintainability.

- **Pylint - Static Code Analysis**
- Evaluates Python code against coding standards and best practices.
- Detects naming convention violations and unused variables.
- Assigns a score to measure code quality.

- **Mypy - Type Checking**
- Ensures type safety using type annotations.
- Catches type mismatches and incorrect function signatures before runtime.
- Makes Python code more robust and maintainable.

- **Black - Code Formatter**
- Automatically reformats code to adhere to PEP 8.
- Enforces strict formatting rules for consistency.
- Eliminates the need for manual code styling.

- **Isort - Import Sorting**
- Organizes imports in a structured and alphabetical manner.
- Groups standard libraries, third-party libraries, and local imports separately.
- Improves code clarity and reduces import conflicts.

- **Bandit - Security Scanner**
- Scans code for security vulnerabilities.
- Detects hardcoded passwords, SQL injection risks, and unsafe function calls.
- Helps identify security flaws early in development.

- **Radon - Complexity Checker**
- Measures code complexity using Cyclomatic Complexity and other metrics.
- Identifies overly complex functions or classes that need refactoring.
- Enhances maintainability and performance.

- **Autopep8 - Auto Formatter**
- Automatically fixes minor PEP 8 violations.
- Corrects extra spaces, incorrect indentation, and missing whitespace.
- Quickly improves code style while maintaining structure.

"""

import argparse
import subprocess
from typing import Dict, Set

# Define available linting tools and their commands
LINTING_COMMANDS: Dict[str, str] = {
    "flake8": "flake8 {dir}",
    "pylint": "pylint {dir}",
    "mypy": "mypy {dir}",
    "black": "black {dir}",
    "isort": "isort {dir}",
    "bandit": "bandit -r {dir}",
    "radon": "radon cc {dir} -a",
    "autopep8": "autopep8 --in-place --recursive {dir}",
}


def run_linting_tools(project_dir: str, skip_tools: str) -> None:
    """
    Runs various linting and code quality tools on the given project directory.
    Allows skipping selected tools via the `skip_tools` parameter.

    :param project_dir: Path to the project directory.
    :param skip_tools: Comma-separated string of tools to skip.
    """
    skip_set: Set[str] = set(skip_tools.split(",")) if skip_tools else set()
    summary_results = {}

    for tool, command in LINTING_COMMANDS.items():
        if tool in skip_set:
            print(f"⏩ Skipping: {tool}")
            summary_results[tool] = "⏩ Skipped"
            continue

        full_command = command.format(dir=project_dir)
        print(f"🔍 Running: {full_command}")

        try:
            subprocess.run(full_command, shell=True, check=True)
            print(f"✅ {tool} completed successfully!")
            summary_results[tool] = "✅ Passed"
        except subprocess.CalledProcessError as e:
            print(f"❌ {tool} failed with error code {e.returncode}")
            summary_results[tool] = f"❌ Failed (Error {e.returncode})"

    # Print final summary

    print("\n📌 **Linting Summary** 📌")
    for tool, status in summary_results.items():
        print(f"- {tool}: {status}")

    print("\n✅ All checks completed!")


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for project directory and tools to skip.

    :return: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Run linting & code quality tools on a project."
    )

    parser.add_argument(
        "project_dir",
        nargs='?',
        default="Ai_Meeting_Coordinator/",
        help="Path to the project directory (default: 'src/')",
    )

    parser.add_argument(
        "--skip",
        default="",
        help="Comma-separated list of tools to skip (e.g., 'black,isort')",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    run_linting_tools(args.project_dir, args.skip)
