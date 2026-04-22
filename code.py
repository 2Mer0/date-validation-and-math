import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    #for december we get the diff from december the current and january the next
    if month == 12:
        return (datetime.date(year + 1, 1, 1) - datetime.date(year, 12, 1)).days
    else:
      #from january to november we get the difference of the current month and the next
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    #we have to validate all three criteria's  and we do so with an if statements with 3 ands in between because if one is false all is false ^^
    if (datetime.MAXYEAR >= year >= datetime.MINYEAR) and (12 >= month >= 1) and (1 <= day <= days_in_month(year, month)):
        return True
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    # Check if either date is invalid
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0

    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # If the second date is before the first date, return 0
    if date2 < date1:
        return 0

    days_difference = (date2 - date1).days
    return days_difference


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    if not is_valid_date(year, month, day):
        return 0
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    if birth_date > today:
        return 0
    return (today - birth_date).days



if __name__ == "__main__":
    print(age_in_days(2005, 9, 10))