📌 Overview
This project is a Python utility module that performs common date-related calculations using the built‑in datetime library.
It includes functions for determining days in a month, validating dates, calculating the number of days between two dates, and computing a person's age in days.

🧠 Features
The project provides the following functionality:

✅ Determine the number of days in a given month
✅ Validate whether a date is real and within allowable limits
✅ Calculate the number of days between two dates
✅ Calculate age in days from a given birthdate
✅ Safely handle invalid or future dates


⚙️ Functions Included
days_in_month(year, month)

Returns the number of days in the given month
Correctly handles leap years using datetime

is_valid_date(year, month, day)

Checks if a date is valid
Ensures:

Year is within allowed datetime range
Month is between 1–12
Day exists in the specified month



days_between(year1, month1, day1, year2, month2, day2)

Returns the number of days between two dates
Returns 0 if:

Either date is invalid
The second date is earlier than the first



age_in_days(year, month, day)

Calculates age in days from a birthdate to today
Returns 0 if:

The date is invalid
The date is in the future

▶️ Example Usage
print(age_in_days(2005, 9, 10))
<7529>
🛠️ Technologies Used

Python 3
Built‑in datetime module


▶️ How to Run

Make sure Python 3 is installed
Save the file as date_utils.py
Run the script:
python date_utils.py
The script will print the age in days for the example date


📚 Educational Purpose
This project was created for learning and coursework purposes and demonstrates:

Function decomposition
Input validation
Date arithmetic
Defensive programming
Practical use of Python’s datetime module


✅ Notes

All calculations rely on Python’s standard library
No third‑party packages required
Code includes detailed comments for clarity
