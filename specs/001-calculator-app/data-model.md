# Data Model: Calculator App

## Internal Entities

### `Token`
Represents the smallest unit of a calculation.
- **Type**: `OPERAND` | `OPERATOR` | `PAREN_OPEN` | `PAREN_CLOSE`
- **Value**: `float` (for operands) or `string` (for operators/parentheses)

### `CalculationState`
Maintains the current context of the user's input.
- **Expression**: `string` (raw input from user)
- **Tokens**: `List[Token]` (parsed tokens)
- **Result**: `float` or `Error` (computed result)

## Processing Flow
1. **Input**: String ("10 + 5")
2. **Tokenizer**: List of Tokens `[10.0, "+", 5.0]`
3. **Parser**: RPN Order `[10.0, 5.0, "+"]`
4. **Evaluator**: Result `15.0`
