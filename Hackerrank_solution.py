


#Question 1:



#Question 2:

def rotateLeft(d, arr):
    for i in range(d):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=temp    
    return arr  

#Question 3:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    answer= ["Louise","Richard"]
    count = 0
    summer = n
    while summer!=1:
        modulus = summer - 2**(math.log(summer)//math.log(2))
        if modulus!=0:
            summer = modulus
        else:
            summer = summer/2
        if summer!=1:
            count+=1
    return answer[count%2]                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()





#Question 4:
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    format_ = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format_)
    t2 = datetime.strptime(t2, format_)
    return str(int(abs((t1-t2).total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

