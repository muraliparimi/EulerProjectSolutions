#!/usr/bin/python

"""Even Fibonacci numbers below 4000000"""

class EvenFibonacciNumbers(object):
    def __init__(self, Max_limit):
        self.limit = Max_limit
    
    def generateFibonacci(self):
        res=[1,2]
        while res[-1] <self.limit:
            res.append(res[-1]+res[-2])
        return res

    def EvenFibonacciSum(self,x):
        sum=0
        for num in x:
            if (num%2==0):
                sum+=num
        return sum

def main():
    EvenFib = EvenFibonacciNumbers(4000000)
    ListOfFibonacciNumbers = EvenFib.generateFibonacci()
    print EvenFib.EvenFibonacciSum(ListOfFibonacciNumbers)

if __name__ == '__main__':
    main()
