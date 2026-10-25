# Business Rules for Cloudstep Software

MID_TIER_SEATS = 10
TOP_TIER_SEATS = 50
MID_TIER_RATE = 0.07
TOP_TIER_RATE = 0.16

NO_DISCOUNT = 0.0
ONBOARDING_FEE = 60.0
ONBOARDING_FEE_LIMIT = 400.0
CONTRACT_REVIEW_LIMIT = 5000.0
TRAINER_SEATS = 25
TRAINER_TOTAL_LIMIT = 3000.0


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return the license cost before any discount."""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if seats >= TOP_TIER_SEATS and education:
        return TOP_TIER_RATE
    elif seats >= MID_TIER_SEATS:
        return MID_TIER_RATE
    else:
        return NO_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Return the discounted cost plus the onboarding fee when it applies."""
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    total = cost - cost * discount
    if total <= ONBOARDING_FEE_LIMIT:
        total = total + ONBOARDING_FEE
    return total


def needs_contract_review(total: float) -> bool:
    """Return True when the license total needs a contract review."""
    return total > CONTRACT_REVIEW_LIMIT


def gets_trainer(seats: int, total: float) -> bool:
    """Return True when the order gets a dedicated trainer."""
    return seats >= TRAINER_SEATS or total > TRAINER_TOTAL_LIMIT


def total_licensed(orders: list) -> float:
    """Return the sum of the license totals for every order."""
    running_total = 0.0
    for order in orders:
        running_total = running_total + calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
    return running_total


def largest_license(orders: list) -> str:
    """Return the company of the order with the largest license total."""
    largest_total = 0.0
    largest_company = ""
    for order in orders:
        total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        if total > largest_total:
            largest_total = total
            largest_company = order["company"]
    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """Return one line of the report."""
    review_text = "no"
    if contract_review:
        review_text = "yes"
    trainer_text = "no"
    if trainer:
        trainer_text = "yes"
    return f"{company}: ${total:.2f} | contract review: {review_text} | trainer: {trainer_text}"
