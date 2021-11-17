# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:26:26 2021

@author: touhidiali
"""

class PrimeNumber:
    pnumber = set()
    nonpnumber = set()
    

    def isprime(self, number):
        if not isinstance(number, (int, list)):
            raise TypeError('Number is not integer nor list')
        
        if isinstance(number, list):
            result = tuple(map(self.isprime, number))
            return result
        if number <=0:
            raise ValueError("the number must be a positive ")

        if number in self.nonpnumber:
            return False
        elif number in self.pnumber:

            return True

        if any(map(lambda i: number % i == 0, range(2, number))):
            self.nonpnumber.add(number)
            return False
        else:
            self.pnumber.add(number)
            return True


obj = PrimeNumber()
print(obj.isprime([2, 3, 4, 5, 6, 7]))
print(obj.isprime(13))
print(obj.isprime(16))
