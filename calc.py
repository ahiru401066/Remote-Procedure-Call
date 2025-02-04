from collections import Counter
import math

class Calc:

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def floatToInt(x):
        return math.floor(x)

    @staticmethod
    def nroot(n,x):
        if n <= 0:
            raise "n must be greater than 0"
        if x < 0 and n % 2 == 0:
            raise "Cannot compute even root of negative number"
        return x ** (1 / n)

        return x ** (1 / n)
    
    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def validAnagram(s,t):
        return Counter(s) == Counter(t)

    @staticmethod
    def sort(s):
        return sorted(s)