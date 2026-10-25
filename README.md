# ISM3232 Midterm: Cloudstep Software

**Name:** Eilene Rios
**Version:** Epsilon
**Date:** October 25, 2026

## What This Program Does

This program calculates license totals for Cloudstep Software's scheduling app, that is sold by the seat. It applies the company's discount, onboarding fee, contract review, and trainer rules to each order. It then prints a report with one line per order and a summary of the totals, the average, the largest order, and how many orders need a contract review or a trainer.

## Business Rules

1. The license cost is the price per seat times the number of seats.
2. Orders with fewer than 10 seats get no discount, and orders with 10 to 49 seats get 7% off.
3. Orders with 50 or more seats get 16% off only if the customer is in education then everyone else gets 7%.
4. A $60 onboarding fee is added when the discounted cost is $400 or less.
5. A license total over $5,000 needs a contract review.
6. An order gets a dedicated trainer if it has 25 or more seats or its license total is over $3,000.

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## How to Test

```bash
ruff format .
ruff check .
pytest -v
```

The project has 23 pytest tests.

## Files in This Repository

## Files in This Repository

- `business_rules.py`: has the eight functions for the business rules.
- `main.py`: runs the program and prints the order report.
- `tests/test_business_rules.py`: has my 23 tests for the functions.
- `tests/__init__.py`: an empty file so pytest can find my code.
- `commands.md`: the terminal commands I used and their output.
- `README.md`: explains the project and how to run it.
- `requirements.txt`: the packages the project needs.
- `.gitignore`: tells Git to ignore `.venv/` and `__pycache__/`.

## AI Use Statement

I did not use AI.
