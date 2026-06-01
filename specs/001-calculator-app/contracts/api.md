# API Contract: Calculator Core

## Logic Interface

### `calculate(expression: str) -> Union[float, str]`
The primary entry point for the calculator logic.
- **Input**: A mathematical expression string.
- **Output**: The numeric result as a float, or "Error" for invalid operations (e.g., division by zero).

### `tokenize(expression: str) -> List[Token]`
Internal method to convert string to a structured list.

### `parse_rpn(tokens: List[Token]) -> List[Token]`
Internal method implementing Shunting Yard to reorder tokens.

### `evaluate_rpn(rpn_tokens: List[Token]) -> float`
Internal method to process the RPN list and return the final value.

## Error Handling
- **Division by Zero**: Returns "Error".
- **Invalid Input**: Returns "Error" (e.g., "1 + + 2").
- **Unsupported Characters**: Returns "Error".
