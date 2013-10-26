'''
Created on Oct 26, 2013

@author: shu
'''
import sys
from sample import Calc

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("error : input two numbers")
        exit(1)
    calc = Calc()
    print(calc.add(float(sys.argv[1]), float(sys.argv[2])))
    exit(0)