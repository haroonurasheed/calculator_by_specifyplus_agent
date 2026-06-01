import re
from dataclasses import dataclass
from typing import List, Union

@dataclass
class Token:
    type: str  # 'OPERAND', 'OPERATOR', 'PAREN_OPEN', 'PAREN_CLOSE'
    value: Union[float, str]

PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def tokenize(expression: str) -> List[Token]:
    """Converts a string expression into a list of structured tokens."""
    # Matches numbers (including decimals) and operators/parentheses
    pattern = r'\d+\.?\d*|[\+\-\*\/\(\)]'
    raw_tokens = re.findall(pattern, expression)
    
    tokens = []
    for t in raw_tokens:
        if re.match(r'\d+', t):
            tokens.append(Token('OPERAND', float(t)))
        elif t == '(':
            tokens.append(Token('PAREN_OPEN', t))
        elif t == ')':
            tokens.append(Token('PAREN_CLOSE', t))
        else:
            tokens.append(Token('OPERATOR', t))
    return tokens

def shunting_yard(tokens: List[Token]) -> List[Token]:
    """Converts infix tokens to Reverse Polish Notation (RPN)."""
    output = []
    operators = []
    
    for token in tokens:
        if token.type == 'OPERAND':
            output.append(token)
        elif token.type == 'PAREN_OPEN':
            operators.append(token)
        elif token.type == 'PAREN_CLOSE':
            while operators and operators[-1].type != 'PAREN_OPEN':
                output.append(operators.pop())
            if operators:
                operators.pop()  # Remove '('
        elif token.type == 'OPERATOR':
            while (operators and operators[-1].type == 'OPERATOR' and
                   PRECEDENCE.get(operators[-1].value, 0) >= PRECEDENCE.get(token.value, 0)):
                output.append(operators.pop())
            operators.append(token)
            
    while operators:
        output.append(operators.pop())
    return output

def evaluate_rpn(rpn_tokens: List[Token]) -> float:
    """Evaluates an RPN list of tokens."""
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    
    for token in rpn_tokens:
        if token.type == 'OPERAND':
            stack.append(token.value)
        elif token.type == 'OPERATOR':
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            b = stack.pop()
            a = stack.pop()
            try:
                result = ops[token.value](a, b)
                stack.append(result)
            except ZeroDivisionError:
                raise ZeroDivisionError("Error")
                
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

def calculate(expression: str) -> Union[float, str]:
    """Main entry point for calculating an expression."""
    try:
        # Check for invalid characters
        if re.search(r'[^\d\+\-\*\/\(\)\.\s]', expression):
            return "Error"
            
        tokens = tokenize(expression)
        if not tokens:
            return 0.0
        rpn = shunting_yard(tokens)
        result = evaluate_rpn(rpn)
        return result
    except ZeroDivisionError:
        return "Error"
    except Exception:
        return "Error"
