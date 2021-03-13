## Author: Daniel Hunt
# Date: 3/12/2021
# Description: Solution to https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:             # Constraints as dictated by the problem. 
        for i in range(1, n + 1): # Provides parameters to the range function.  
            print(i, end = "")    # Prints the range of numbers right next to each other by using end = "" to remove the newline seperators. 
