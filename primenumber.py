class PrimeNumber:
    pnumber = []
    nonpnumber = []

    def isprime(self, number):
        if not isinstance(number, (int, list)):
            raise TypeError('Number is not integer nor list')
        if isinstance(number, list):
            result = []
            for num in number:
                result.append(self.isprime(num))
            return result

        if number in self.nonpnumber:
            return False
        elif number in self.pnumber:

            return True

        for i in range(2, number):
            if number % i == 0:
                self.nonpnumber.append(number)
                return False

        self.pnumber.append(number)
        return True


obj = PrimeNumber()
print(obj.isprime([2, 3, 4, 5, 6, 7]))
print(obj.isprime(13))
print(obj.isprime(16))
