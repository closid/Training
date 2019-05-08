#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for f in range(1,n+1):
        print(("#"*f).rjust(n) ) 

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
