def sieve_eratosthenes(n):
    '''
    Sieve of Eratosthenes
    
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    '''
    size = n + 1
    sieve = bytearray(size)
    p = [2]
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i] == 0:
            # for Python 2, 3
            # sieve[i*i::2*i] = [1]*len(sieve[i*i::2*i])
            for j in xrange(i*i, size, 2*i):
                sieve[j] = 1

    return p + [i for i in xrange(3, size, 2) if sieve[i] == 0]

def odd_sieve_eratosthenes(n):
    ub = (n+n%2)//2
    sieve = bytearray(ub)

    for i in xrange(1, int(n**0.5)//2+1):
        if sieve[i] == 0:
            step = 2*i
            start = step*(i+1)
            step += 1
            # for Python 2, 3
            # sieve[start::step] = [1]*len(sieve[start::step])
            for j in xrange(start, ub, step):
                sieve[j] = 1
    if n > 1:
        return [2] + [2*i+1 for i in xrange(1, ub) if sieve[i] == 0]
    else:
        return []    

def sieve_sundaram(n):
    ''' 
    Sieve of Sundaram
    
    https://en.wikipedia.org/wiki/Sieve_of_Sundaram
    '''
    ub = (n-1)//2 + 1
    sieve = bytearray(ub)
    start = 0
    for i in xrange(1, ub):
        start += 4*i
        if start >= ub:
            break
        # for Python 2, 3
        # sieve[start::2*i+1] = [1]*len(sieve[start::2*i+1])
        for j in xrange(start, ub, 2*i+1):
            sieve[j] = 1

    return [2] + [2*i+1 for i in xrange(1, ub) if sieve[i] == 0]

def totient(n):
    size = n + 1
    phi = [i for i in xrange(size)]

    for i in xrange(2, size):
        if phi[i] == i:
            phi[i] = i - 1
            for j in xrange(2*i, size, i):
                phi[j] = (phi[j]//i)*(i-1) 

    return phi

phi = totient

def lprime_div(n):
    size = n + 1
    lpd = [i for i in xrange(size)]

    for i in xrange(2, int(n**0.5)+1):
        if lpd[i] == i:
            for j in xrange(i*i, size, i):
                if lpd[j] == j:            		
                    lpd[j] = i

    return lpd
