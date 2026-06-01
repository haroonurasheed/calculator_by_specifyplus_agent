import sys
from src.calculator.logic import calculate

def main():
    print("--- Python Calculator CLI ---")
    print("Enter expressions (e.g., '2 + 3 * 4') or 'C' to clear, 'quit' to exit.")
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if user_input.lower() in ['c', 'clear']:
                print("0")
                continue
                
            result = calculate(user_input)
            print(result)
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
