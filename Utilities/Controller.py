import random
import string
from datetime import date, timedelta, datetime


def generate_secure_password(length):
    # Ensure minimum length for constraints
    if length < 3:
        length = 3

    # 1. Guarantee required characters
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    # 2. Generate remaining characters
    all_chars = string.ascii_letters + string.digits
    remaining_length = length - 3
    remaining_chars = random.choices(all_chars, k=remaining_length)

    # 3. Combine and shuffle (to ensure random placement)
    password_list = list(upper + lower + digit + ''.join(remaining_chars))
    random.shuffle(password_list)

    return ''.join(password_list)

def get_random_date_components(start_year=1950, end_year=2024):
    """
    Generates a random date within the specified year range and returns
    the day number, month name, and year number.

    Args:
        start_year (int): The earliest year to consider.
        end_year (int): The latest year to consider.

    Returns:
        tuple: (day_number, month_name, year_number)
    """

    # 1. Define the start and end dates for the random range
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    # 2. Calculate the total number of days in the range
    time_difference = end_date - start_date
    total_days = time_difference.days

    # 3. Pick a random number of days to add to the start date
    random_days = random.randint(0, total_days)

    # 4. Calculate the random date
    random_date = start_date + timedelta(days=random_days)

    # 5. Extract the required components
    day_number = random_date.day  # e.g., 25
    month_name = random_date.strftime("%B")  # e.g., 'October'
    year_number = random_date.year  # e.g., 2005

    return str(day_number), month_name, str(year_number)

get_cur_dt = lambda dt_format=None: datetime.now().strftime("%m_%d_%Y") if dt_format is None else \
            datetime.now().strftime(dt_format)
get_cur_time = lambda time_format=None: datetime.now().strftime("%H_%M_%S") if time_format is None else \
            datetime.now().strftime(time_format)
get_random_text = lambda L: random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_letters, k=L - 1))