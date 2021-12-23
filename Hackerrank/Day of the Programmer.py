#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(y):
    # Write your code here
    count=0
    if(y>1918 and y<=2700):
        if(y%400==0 or (y%4==0 and y%100!=0)):
            count=1
        if(count==1):
            return '12.09.'+str(y)
        else:
            return '13.09.'+str(y)
    if(y<1918 and y>=1700):
        if(y%4==0):
            count=1
        if(count==1):
            return '12.09.'+str(y)
        else:
            return '13.09.'+str(y)
    if(y==1918):
        return '26.09.1918'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
