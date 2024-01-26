Most Active Cookies

The file most_active_cookies.py consists of the command line program in your preferred language to process the log file and return the most active cookie for a specific day. The runtime complexity of the search function most_active_cookie() is linear with respect to the number of lines in the log file

The file most_active_cookies_test.py is the tester file of most_active_cookies.py. 


## Table of Contents

- [Developers Guide]
- [Usage]
- [Testing]

## Developers Guide

Put the CSV file in the same directory as the python program files, before running the commands with most_active_cookies

## Usage

The CLI program takes two arguments:

-f, The CSV file path
-d, the date argument formatted as YYYY-MM-DD


Example:
We’d execute the program like this to obtain the most active cookie for 9th Dec 2018.
$ python3 most_active_cookie.py -f cookie_log.csv -d 2018-12-09

We define the most active cookie as one seen in the log the most times during a given day,
so the program will return one or more cookies as below:

Most active cookie(s):
AtY0laUfhglK3lC7

## Testing 

To run the tests for the `most_active_cookies` program, follow these steps:

1. Make sure you have the necessary dependencies installed.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `most_active_cookies_test.py` file is located.
4. Run the command `python3 most_active_cookies_test.py` to execute the test suite.
5. Check the output to see if all the tests passed.

If any of the tests fail, review the error messages to identify the issue and make the necessary adjustments to the code.
