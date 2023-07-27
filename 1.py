
def sum_leap_years(date_list):
    leap_years = []
    
    for year, _ in date_list:
        if year % 4 == 0:
            leap_years.append(year)
    
    return sum(leap_years)

date_list = [(1994, 3), (2001, 7), (2010, 11), (1998, 5), (2022, 12)]
result = sum_leap_years(date_list)
print(result) 
