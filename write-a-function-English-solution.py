## Author: Daniel Hunt
# Date: 3/16/2021
# Description: Takes a year as an input and outputs whether or not it is a leap year.
#
def is_leap(year):
    """
    Description: Calculates whether a year is a leap year or not.
    Input: (int) Year 
    Output: (boolean) Whether it is a leap year or not.
    """
    
    leap = False
    
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                leap = True

            else:
                leap = False
        else:
            leap = False
    else:
        leap = False
    
    return leap

year = int(input())
