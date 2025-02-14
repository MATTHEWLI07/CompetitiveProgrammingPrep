import re
from datetime import datetime

def find_valid_dates(document):
    date_pattern = re.compile(r'(?<!\w)(\d{4}-\d{2}-\d{2})(?!\w)')
    valid_dates = []

    for line in document:
        potential_dates = date_pattern.findall(line)
        for date_str in potential_dates:
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                valid_dates.append(date_str)
            except ValueError:
                continue
    
    return valid_dates

n = int(input())
document = [input().strip() for _ in range(n)]
result = find_valid_dates(document)

for date in result:
    print(date)