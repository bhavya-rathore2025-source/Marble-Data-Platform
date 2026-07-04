import random
import uuid

from datetime import datetime
from datetime import timedelta

from config import RANDOM_SEED

random.seed(RANDOM_SEED)


# Generate random date

def random_date(start_date: str, end_date: str) -> str:

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    days = (end - start).days

    return (start + timedelta(
        days=random.randint(0, days)
    )).strftime("%Y-%m-%d")


# Generate future date

def future_date(date_string: str,
                min_days: int,
                max_days: int) -> str:

    base_date = datetime.strptime(date_string, "%Y-%m-%d")

    future = base_date + timedelta(
        days=random.randint(min_days, max_days)
    )

    return future.strftime("%Y-%m-%d")


# Generate random decimal

def random_decimal(min_value: float,
                   max_value: float,
                   digits: int = 2) -> float:

    return round(
        random.uniform(min_value, max_value),
        digits
    )


# Generate business code

def generate_code(prefix: str,
                  number: int,
                  width: int = 4) -> str:

    return f"{prefix}{number:0{width}}"


# Generate UUID

def random_uuid() -> str:

    return str(uuid.uuid4())


# Return True based on probability

def chance(percent: float) -> bool:

    return random.random() < (percent / 100)


# Pick random item from list

def random_choice(values: list):

    return random.choice(values)


def weighted_choice(options, weights):
    """
    Select a single value using weighted probabilities.

    Args:
        options (list): List of possible values.
        weights (list): Relative probability for each option.

    Returns:
        Any: Randomly selected value.
    """
    return random.choices(options, weights=weights, k=1)[0]
