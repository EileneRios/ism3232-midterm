# Cloudstep Software Pytests

from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


# calculate_license_cost (rule 1)
def test_license_cost_is_price_times_seats():
    assert round(calculate_license_cost(13.00, 20), 2) == 260.00


# get_seat_discount (rules 2 and 3)
def test_discount_9_seats_is_none():
    assert get_seat_discount(9) == 0.0


def test_discount_10_seats_is_mid_tier():
    assert get_seat_discount(10) == 0.07


def test_discount_49_seats_education_is_mid_tier():
    assert get_seat_discount(49, True) == 0.07


def test_discount_50_seats_education_is_top_tier():
    assert get_seat_discount(50, True) == 0.16


def test_discount_50_seats_not_education_is_mid_tier():
    assert get_seat_discount(50, False) == 0.07


# calculate_license_total (rule 4)
def test_total_fee_added_at_exactly_400():
    assert round(calculate_license_total(400.00, 1), 2) == 460.00


def test_total_no_fee_just_over_400():
    assert round(calculate_license_total(400.01, 1), 2) == 400.01


def test_total_with_mid_tier_discount_and_fee():
    assert round(calculate_license_total(13.00, 20), 2) == 301.80


def test_total_education_gets_top_tier_discount():
    assert round(calculate_license_total(50.00, 60, True), 2) == 2520.00


# needs_contract_review (rule 5)
def test_review_not_needed_at_exactly_5000():
    assert needs_contract_review(5000.00) is False


def test_review_needed_just_over_5000():
    assert needs_contract_review(5000.01) is True


# gets_trainer (rule 6)
def test_trainer_at_exactly_25_seats():
    assert gets_trainer(25, 0.00) is True


def test_no_trainer_at_24_seats():
    assert gets_trainer(24, 0.00) is False


def test_no_trainer_at_exactly_3000_total():
    assert gets_trainer(1, 3000.00) is False


def test_trainer_just_over_3000_total():
    assert gets_trainer(1, 3000.01) is True


# total_licensed
def test_total_licensed_adds_every_order():
    orders = [
        {"company": "A", "seat_price": 40.00, "seats": 5, "education": False},
        {"company": "B", "seat_price": 400.00, "seats": 9, "education": False},
    ]
    assert round(total_licensed(orders), 2) == 3860.00


def test_total_licensed_empty_list_is_zero():
    assert total_licensed([]) == 0.0


# largest_license
def test_largest_license_finds_biggest_total():
    orders = [
        {"company": "Small", "seat_price": 40.00, "seats": 5, "education": False},
        {"company": "Big", "seat_price": 400.00, "seats": 9, "education": False},
    ]
    assert largest_license(orders) == "Big"


def test_largest_license_tie_returns_first():
    orders = [
        {"company": "First", "seat_price": 100.00, "seats": 5, "education": False},
        {"company": "Second", "seat_price": 100.00, "seats": 5, "education": False},
    ]
    assert largest_license(orders) == "First"


def test_largest_license_empty_list_is_empty_string():
    assert largest_license([]) == ""


# format_license_line
def test_format_line_all_no():
    line = format_license_line("Pine Books", 260, False, False)
    assert line == "Pine Books: $260.00 | contract review: no | trainer: no"


def test_format_line_all_yes():
    line = format_license_line("Summit College", 6300, True, True)
    assert line == "Summit College: $6300.00 | contract review: yes | trainer: yes"
