def sieve_eratosthenes(n):
    size = n + 1
    sieve = bytearray(size)

    for i in xrange(2, int(n**0.5)+1):
        if sieve[i] == 0:
            for j in xrange(i*i, size, i):
                sieve[j] = 1

    return [i for i in xrange(2, size) if sieve[i] == 0]

def sieve_sundaram(n):
    size = n + 1
    sieve = bytearray(size)
    ub = (n-1)//2 + 1
    start = 0
    
    for i in xrange(1, ub):
        start += 4*i
        if start >= ub:
            break
        for j in xrange(start, ub, 2*i+1):
            sieve[j] = 1
    return [2] + [2*i+1 for i in xrange(1, ub) if sieve[i] == 0]
  
