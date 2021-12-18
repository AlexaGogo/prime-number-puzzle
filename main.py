# My Python might be a bit rough so I'm sorry in advance. I figured attempting this problem was a good excuse to
# finally learn how to code in it.

maxit = 20000  # find_prime returns if target does not exist in fib(maxit)


# Learned about Miller-Rabin primality test after multiple failed attempts at building a quick prime checker.
# Found Python version of test claiming correct answers for n up to 341550071728321, which, if true, should work
# perfectly for our intended purposes. Used it here.
# Code found from: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N

# Note: I opted to keep all cases in for versatility

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

# End of copied code


# Simple translation function; only works with given alphabet map

def decode(n):
    alphamap = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                23: 'X', 24: 'Y', 25: 'Z'}

    secretword = ""

    while n != 0:
        key = (int(n % 100) % 26)
        secretword = alphamap.get(key) + secretword
        n = int(n / 100)

    return secretword


# Modified base code from https://www.programiz.com/python-programming/examples/fibonacci-sequence

def find_prime(nsize, nocc):
    # first two fib terms
    n1, n2 = 0, 1

    workstr = ""
    pcount = 0
    prime = -1

    it = 0

    while it < maxit:
        workstr += str(n2)

        if len(workstr) >= nsize:
            i = 0

            while i <= (len(workstr) - nsize):
                tempstr = workstr[i:i + nsize]

                if is_prime(int(tempstr)):
                    pcount += 1

                    if pcount == nocc:
                        print("prime #" + str(pcount) + " is " + tempstr)
                        prime = int(tempstr)
                        break
                i += 1

            workstr = workstr[(len(workstr) - (nsize - 1)):]

        if pcount == nocc:
            break

        nth = n1 + n2
        # update fib values
        n1 = n2
        n2 = nth
        it += 1

    return prime


def main():
    print("Let's solve your riddle!\n")

    answer = ""

    nit = int(input("How many prime numbers are you looking for? "))

    it = 0

    while it < nit:
        print("Prime #" + str(it + 1) + ":")
        nsize = int(input("# of digits in target prime: "))

        if nsize >= 15:
            print("Warning: internal prime checker may be inaccurate for numbers > 341550071728321")

        nocc = int(input("target is the ____ prime that occurs in Fib(n): "))

        prime = find_prime(nsize, nocc)

        if prime > -1:
            word = decode(prime)
            print("The decoded word is: " + word)
            answer = answer + word + " "
        else:
            print("Sorry, prime not found")

        it += 1

    print("Your answer is: " + answer + "!")


main()
