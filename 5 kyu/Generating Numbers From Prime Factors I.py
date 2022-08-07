from functools import reduce
from itertools import product

def count_find_num(primesL, limit):
    results = []
    final_results = []
    for prime_num in primesL:
        prime_mulitiplied = 1
        power = 1
        primes_mulitiplied = []
        while prime_mulitiplied <= limit:
            prime_mulitiplied = prime_num ** power
            power += 1
            if prime_mulitiplied <= limit:
                primes_mulitiplied.append(prime_mulitiplied)
        results.append(primes_mulitiplied)
    for multiplies_primes in list(product(*results)):
        result = ((reduce(lambda x,y: x*y, multiplies_primes)))
        if result <= limit:
            final_results.append(result)
    return final_results and [len(final_results), max(final_results)] or []


print(count_find_num([2, 3], 200))