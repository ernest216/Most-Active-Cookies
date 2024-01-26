import argparse
from collections import defaultdict

def is_valid_date(date):
    try:
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
            return False
    except ValueError:
        return False
    return True

def most_active_cookie(filename, date):
    active_cookies = defaultdict(int)

    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            try:
                cookie, timestamp_str = line.strip().split(',')
                if timestamp_str.startswith(date):
                    active_cookies[cookie] += 1
            except ValueError as e:
                print(f"Error processing line {line_num}: {e}")

    max_count = 0
    most_active_cookies = []

    for cookie, count in active_cookies.items():
        if count > max_count:
            max_count = count
            most_active_cookies = [cookie]
        elif count == max_count:
            most_active_cookies.append(cookie)

    return most_active_cookies

def main():
    parser = argparse.ArgumentParser(description='Find the most active cookie for a specific day.')
    parser.add_argument('-f', '--filename', required=True, help='Cookie log file name')
    parser.add_argument('-d', '--date', required=True, help='Date in the format YYYY-MM-DD')
    args = parser.parse_args()

    if not is_valid_date(args.date):
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return
    
    result = most_active_cookie(args.filename, args.date)

    if result:
        print("Most active cookie(s):")
        for cookie in result:
            print(cookie)
    else:
        print('No cookies found for the specified date.')

if __name__ == '__main__':
    main()

