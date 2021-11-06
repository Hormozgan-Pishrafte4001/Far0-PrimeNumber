class PrimeNumber:
    pnumber = []
    nonpnumber = []

    def isprime(self, number):
        if type(number) != int:
            raise TypeError('Number is not integer')
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
