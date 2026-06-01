# Quickstart: Calculator Development

## Environment Setup

1. **Python Version**: Ensure Python 3.10+ is installed.
2. **Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. **Dependencies**:
   ```bash
   pip install pytest
   ```

## Running Tests
```bash
pytest
```

## Running the App
```bash
PYTHONPATH=. python3 -m src.calculator.cli
```
