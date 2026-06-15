"""
Project Euler Problem 19: Counting Sundays

Problem Statement:
------------------
How many Sundays fell on the first day of the month during the twentieth century
(from 1 January 1901 to 31 December 2000)?

Given Facts:
------------
1. 1 Jan 1900 was a Monday.
2. Thirty days has September, April, June, and November.
3. All the rest have 31 days, except February:
   - 28 days in a normal year.
   - 29 days in a leap year.
4. A leap year occurs when a year is divisible by 4.
   (For this problem, the years considered are 1901–2000, so this simplified
   leap year rule works correctly.)

Approach:
---------
- Store the number of days in each month using a dictionary.
- Track the running day count from 1 Jan 1900.
- Since 1 Jan 1900 was a Monday, initialize the day counter accordingly.
- For each month between January 1901 and December 2000:
    * Check whether the first day of the month is a Sunday.
    * If it is, increment the Sunday counter.
    * Add the number of days in the current month to move to the next month.
    * Adjust February for leap years.

Logic:
------
The variable 'day' represents the total number of days elapsed since
1 Jan 1900. If day % 7 == 0, then the first day of the current month
falls on a Sunday.

Returns:
--------
int:
    Total number of Sundays that occurred on the first day of a month
    between 1 Jan 1901 and 31 Dec 2000.
"""

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


def countingSundays():
    """
    Count the number of Sundays that fell on the first day of a month
    during the twentieth century (1901–2000).

    Returns
    -------
    int
        Number of Sundays that occurred on the first day of a month.
    """

    # Day offset where 1 Jan 1901 starts.
    # Using 1 Jan 1900 = Monday as the reference point.
    day = 2
    sunday_count = 0

    for year in range(1901, 2001):

        for month in months:

            # Check if the first day of the current month is Sunday
            if day % 7 == 0:
                sunday_count += 1

            days = months[month]

            # Add one extra day for February in leap years
            if month == "February" and year % 4 == 0:
                days += 1

            # Move to the first day of the next month
            day += days

    return sunday_count


print("Sundays:", countingSundays())