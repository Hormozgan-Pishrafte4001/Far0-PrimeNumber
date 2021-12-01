# -*- coding: utf-8 -*-

class PrimeNumber:
    pnumber = set()
    nonpnumber = {1, }

    def isprime(self, number):
        if not isinstance(number, int):
            try:
                result = tuple(map(self.isprime, number))
                return result
            except TypeError as e:
                raise e

        if number <= 0:
            raise ValueError("the number must be a positive ")

        if number in self.nonpnumber:
            return False

        if number in self.pnumber:
            return True

        if any(map(lambda i: number % i == 0, range(2, number))):
            self.nonpnumber.add(number)
            return False
        else:
            self.pnumber.add(number)
            return True

    def countprime(self, end, start=0):
        count = 0
        for i in range(start+1, end):
            if self.isprime(i):
                count += 1
        return count


obj = PrimeNumber()
"""
print(obj.isprime([2, 3, 4, 5, 6, 7]))
print(obj.isprime(13))
print(obj.isprime(16))
print(obj.countprime(5, 30))
print(obj.isprime({1, 2, 3, 4, 5, 6, 127}))
print(obj.isprime(range(5, 255)))
print(obj.isprime({1: "Hello", 2: "Bye", 3: "Salaams"}))
"""
print(obj.isprime(None))
