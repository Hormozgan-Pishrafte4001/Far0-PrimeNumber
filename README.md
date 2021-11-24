# Far0-PrimeNumber
The first set of exercises of FarooqKZ's classes during screenshares for AP4001 in Hormozgan University

## Sessions records

You can watch records of these classes in [this PeerTube channel](https://peertube.linuxrocks.online/c/ap4001/videos) in Persian language.

## Teachers

 - Professor: Dr. Saybani
 - Teacher Assistant: Farooq Karimi Zadeh

## Authors (in order)

 - Salime Daryanavard: `isprime()` function
 - Neda Nazifi: `PrimeNumber` class
 - Kimiya Mohazzabi : add the functionality to `isprime()` to accept list of numbers and converting for loops to map
 - Erfan Bagheri:   Add `countprime(start, end)` and `countprime(end)` 

## ToDos

 - [x] Write `isprime()` function
 - [x] Write `PrimeNumber` class and use `isprime()` in it
 - [x] Make the `PrimeNumber` class save checked numbers in its attributes so that `isprime()` won't need to compute everything from scratch everytime.
 - [x] Add the functionality to `isprime()` method accept a list of numbers or a number. In the case it is a list, return a tuple of bools.
 - [x] Make `isprime()` raise `ValueError` if input number(s) is/are smaller than zero.
 - [ ] Add the functionality to `isprime()` to accept any ordered container.
 - [x] Make `isprime()` use `map()` for single prime number check.
 - [x] Make `isprime()` use `map()` for multiple prime number check.
 - [x] Make `PrimeNumber` use Python `set`s for storing checked numbers. Compare the performance with `list`.
 - [x] Write `countprime(end)` method returning the number of all primes smaller than `end`
 - [x] Write `countprime(start, end)` method returning the number of all primes between `start` and `end`
 - [ ] Write `iterprime(start=2, end)` yielding prime numbers from `start` to `end-1`
 - [ ] Write `range(start=2, end)` method returning a `PrimeRange` instance.


## PrimeRange ToDos

 - Write `PrimeRange` class initialized with `start=2` and `end`, saves a list of prime numbers in its state.
 - Write `__contains__` magic method for the class.
 - Write `__len__` magic method for the class.
 - Write `__str__` magic method for the class.

## CLI for PrimeNumber

...

## GUI for PrimeNumber

...
