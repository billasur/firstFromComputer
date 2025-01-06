def primeFactors(n):
    q=1
    primeFactors = []
    for i in range(2,n+1):
        if isPrime(i) != False:
            q = i
            if n % q ==0:
                primeFactors.append(q)
    print(primeFactors)

def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False



n = int(input())
primeFactors(n)

