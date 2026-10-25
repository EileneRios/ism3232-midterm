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
