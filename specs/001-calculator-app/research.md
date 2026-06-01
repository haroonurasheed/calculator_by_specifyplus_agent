# Research: Calculator App Logic & Structure

## Problem Statement
The goal is to build a robust calculator that supports basic arithmetic (+, -, *, /), decimal numbers, and chained operations following PEMDAS order of operations.

## Options Considered

### 1. Built-in `eval()`
- **Pros**: Extremely simple to implement; natively handles PEMDAS.
- **Cons**: Severe security risk (code injection); hard to control error handling specifically for calculator-only logic.
- **Decision**: Rejected due to security concerns and the "Accuracy First" and "Reliability & Stability" principles in the constitution.

### 2. Shunting Yard Algorithm (RPN)
- **Pros**: Secure (no execution of arbitrary code); explicit control over operator precedence (PEMDAS); easy to test individual components (tokenizer, parser, evaluator).
- **Cons**: More complex to implement than `eval()`.
- **Decision**: Selected. It aligns with the constitution's focus on accuracy, testability, and reliability.

## Proposed Architecture

### 1. Tokenizer
Responsible for breaking the input string (e.g., "2 + 3.5 * 4") into a list of tokens: `[2, "+", 3.5, "*", 4]`.

### 2. Parser (Shunting Yard)
Converts the infix notation (tokens) into Reverse Polish Notation (RPN) using a stack for operators.

### 3. Evaluator
Processes the RPN list to compute the final result.

## Technology Stack
- **Language**: Python 3.x (chosen for its strong standard library and readability).
- **Testing**: `pytest` (standard, powerful, and supports TDD as mandated).
- **UI**: CLI initially, with a structure that allows for a future GUI/Web interface.

## Project Structure
```text
src/
├── calculator/
│   ├── __init__.py
│   ├── logic.py       # Core Shunting Yard implementation
│   └── cli.py         # Entry point for CLI interaction
tests/
├── unit/
│   ├── test_logic.py  # Comprehensive tests for arithmetic and PEMDAS
│   └── test_cli.py    # Tests for UI/Error handling
```

## Risk Analysis
- **Floating Point Precision**: Python's `float` uses IEEE 754. For a basic calculator, this is usually acceptable, but we should be aware of `0.1 + 0.2 != 0.3`.
- **Division by Zero**: Must be explicitly caught in the evaluator.
