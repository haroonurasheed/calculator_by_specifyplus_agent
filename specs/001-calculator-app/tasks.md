# Tasks: Calculator App

**Input**: Design documents from `/specs/001-calculator-app/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: `src/calculator/`, `tests/unit/`
- [ ] T002 [P] Initialize Python project and install `pytest`
- [ ] T003 [P] Create `src/calculator/__init__.py` and `tests/__init__.py`

---

## Phase 2: Foundational (Core Logic)

**Purpose**: Implement the Shunting Yard engine which ALL user stories depend on

- [ ] T004 Define `Token` data classes and `PRECEDENCE` mapping in `src/calculator/logic.py`
- [ ] T005 Implement `tokenize(expression: str)` in `src/calculator/logic.py`
- [ ] T006 Implement `shunting_yard(tokens)` to convert infix to RPN in `src/calculator/logic.py`
- [ ] T007 Implement `evaluate_rpn(tokens)` in `src/calculator/logic.py`
- [ ] T008 Implement wrapper `calculate(expression: str)` in `src/calculator/logic.py`

**Checkpoint**: Core engine ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Support addition, subtraction, multiplication, and division for simple calculations.

**Independent Test**: Run `pytest tests/unit/test_logic.py` with basic arithmetic cases.

### Tests for User Story 1

- [ ] T009 [P] [US1] Create unit tests for basic addition/subtraction in `tests/unit/test_logic.py`
- [ ] T010 [P] [US1] Create unit tests for multiplication/division in `tests/unit/test_logic.py`
- [ ] T011 [P] [US1] Create unit tests for chained operations (PEMDAS) in `tests/unit/test_logic.py`

### Implementation for User Story 1

- [ ] T012 [US1] Ensure `evaluate_rpn` handles basic operators (+, -, *, /)
- [ ] T013 [US1] Implement CLI interface in `src/calculator/cli.py` to accept expression and print result
- [ ] T014 [US1] Validate CLI interaction with manual smoke tests (2 + 3 = 5)

**Checkpoint**: MVP Ready - Basic calculator functional via CLI.

---

## Phase 4: User Story 2 - Clearing the Display (Priority: P2)

**Goal**: Reset the calculator state to start a new calculation.

**Independent Test**: Verify CLI can handle multiple inputs or a specific 'C' command if stateful.

### Implementation for User Story 2

- [ ] T015 [US2] Implement 'Clear' logic in `src/calculator/cli.py` (e.g., reset current input loop)
- [ ] T016 [US2] Add 'C' command handling to the CLI input loop

---

## Phase 5: User Story 3 - Error Handling (Priority: P3)

**Goal**: Notify user of invalid operations (Division by Zero, Syntax Error).

**Independent Test**: Run `pytest tests/unit/test_logic.py` with error cases and verify "Error" output.

### Tests for User Story 3

- [ ] T017 [P] [US3] Add unit tests for division by zero in `tests/unit/test_logic.py`
- [ ] T018 [P] [US3] Add unit tests for invalid syntax (e.g., "2 + + 3") in `tests/unit/test_logic.py`

### Implementation for User Story 3

- [ ] T019 [US3] Update `evaluate_rpn` to catch `ZeroDivisionError` and return "Error"
- [ ] T020 [US3] Update `calculate` or `shunting_yard` to catch parsing errors and return "Error"

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T021 [P] Update `specs/001-calculator-app/quickstart.md` with final run instructions
- [ ] T022 Final code cleanup and docstrings in `src/calculator/logic.py`
- [ ] T023 Run all tests one final time to ensure no regressions

---

## Dependencies & Execution Order

1. **Setup (Phase 1)** must be completed first.
2. **Foundational (Phase 2)** is critical and blocks all User Stories.
3. **User Story 1 (P1)** is the MVP and should be completed before P2/P3.
4. **User Story 3 (P3)** can be worked on in parallel with P1 implementation if tests are ready.
