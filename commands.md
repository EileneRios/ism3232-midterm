# Terminal Record: Cloudstep Software

## 1. Building the project

```bash
cd ~
mkdir ism3232-midterm && cd ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
touch business_rules.py main.py command.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
mv command.md commands.md
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
git init && git add . && git status
git commit -m "Part 1: Set up project structure"
git remote add origin https://github.com/EileneRios/ism3232-midterm.git
git branch -M main && git push -u origin main
```

## 2. The Virtual Environment

```bash
which python3
```
```
/Users/eilene/ism3232-midterm/.venv/bin/python3
```

The path ends in .venv/bin/python3, this shows that python3 is running from the project's virtual environment.

## 3. The Project Structure 

```bash
tree -L 2
```
```
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```

The `__pycache__` folders are on my computer but not in my GitHub repository, because `.gitignore` excludes them since Python creates them automatically when the code runs.

## 4. Every Function and Test

```bash
rg 'def '
```
```
business_rules.py
16:def calculate_license_cost(seat_price: float, seats: int) -> float:
21:def get_seat_discount(seats: int, education: bool = False) -> float:
31:def calculate_license_total(
43:def needs_contract_review(total: float) -> bool:
48:def gets_trainer(seats: int, total: float) -> bool:
53:def total_licensed(orders: list) -> float:
63:def largest_license(orders: list) -> str:
77:def format_license_line(

tests/test_business_rules.py
16:def test_license_cost_is_price_times_seats():
21:def test_discount_9_seats_is_none():
25:def test_discount_10_seats_is_mid_tier():
29:def test_discount_49_seats_education_is_mid_tier():
33:def test_discount_50_seats_education_is_top_tier():
37:def test_discount_50_seats_not_education_is_mid_tier():
42:def test_total_fee_added_at_exactly_400():
46:def test_total_no_fee_just_over_400():
50:def test_total_with_mid_tier_discount_and_fee():
54:def test_total_education_gets_top_tier_discount():
59:def test_review_not_needed_at_exactly_5000():
63:def test_review_needed_just_over_5000():
68:def test_trainer_at_exactly_25_seats():
72:def test_no_trainer_at_24_seats():
76:def test_no_trainer_at_exactly_3000_total():
80:def test_trainer_just_over_3000_total():
85:def test_total_licensed_adds_every_order():
93:def test_total_licensed_empty_list_is_zero():
98:def test_largest_license_finds_biggest_total():
106:def test_largest_license_tie_returns_first():
114:def test_largest_license_empty_list_is_empty_string():
119:def test_format_line_all_no():
124:def test_format_line_all_yes():
```

business_rules.py defines 8 functions and tests/test_business_rules.py defines 23 tests.

## 5. Which Files Print

```bash
rg -l 'print'
```
```
main.py
```

main.py is the only Python file that prints, because business_rules.py only returns values and main.py prints them.

## 6. The Commit History 

```bash
git log --oneline
```
```
60c2027 (HEAD -> main, origin/main) Test for list function and report lines
c5ccbf3 Test for license total, contract review and trainer
656de19 Test for license cost and seat discount
40d6a75 Add main.py order report
80ce495 Add Business Rules Functions
f4ac9ed Part 1 commands
939a8a7 Part 1: Set up project structure
```

There are 7 commits at this point.