## Author: Daniel Hunt
# Date: 3/16/2021
# Description: Takes a year as an input and outputs whether or not it is a leap year.
#
## Author: Daniel Hunt
# Date: 3/16/2021
# Description: Takes a year as an input and outputs whether or not it is a leap year.
#
year = int(input())

def is_leap(year):
    
    """
    Description: Calculates whether a year is a leap year or not.
    Input: (int) Year 
    Output: (boolean) Whether it is a leap year or not.
    """
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
                              
  

print(is_leap(1992))
