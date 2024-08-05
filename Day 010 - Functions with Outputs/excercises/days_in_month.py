def is_leap(year):
    """
    Determine if a given year is a leap year.

    A leap year is exactly divisible by 4, except for years that are exactly divisible by 100.
    However, years that are exactly divisible by 400 are leap years.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """
    Determine the number of days in a given month of a specific year.

    This function accounts for leap years when checking the number of days in February.

    Args:
        year (int): The year of the date.
        month (int): The month of the date (1 for January, 2 for February, etc.).

    Returns:
        int: The number of days in the specified month.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # First check the year.
    if is_leap(year) and month == 2:
        # Check the month if it is February.
        return 29
    else:
        return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

