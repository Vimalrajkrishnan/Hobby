# Python 3.x code to demonstrate star pattern
import time
# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(n-1):
        print(' '*(n-i-1),'*'*(2*i+1))
    for i in range(n-1,-1,-1):
        print(' '*(n-i-1),'*'*(2*i+1))
    for i in range(n-1,0,-1):
        print(' '*(n-i-1),'*'*(2*i+1))
    for i in range(n):
        print(' '*(n-i-1),'*'*(2*i+1))
pypart(5)
