import math

def factorial(n):
    ans = [1,1]

    for i in range(2, n+1):
        ans.append(ans[-1]*i)
    
    return ans[-1]

def choose(n,r):
    if n>=r>=0:
        top = factorial(n)
        bottom = (factorial(r)) * (factorial(n-r))
        return top/bottom
    else:
        print("Can't execute") 


def binomial_distribution(n,p,x,is_cdf):
    # n: number of trials
    # p: probability of success in single trial
    # x: number of success

    stdev = math.sqrt(n*p*(1-p))
    print(f"Standard deviation is {stdev}")

    mean = n*p
    print(f"mean value is {mean}")
    
    # Formula
    # P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)

    # single x probability
    if is_cdf:
        
        ans = 0
        for i in range(x+1):
            ans += choose(n,i) * (p**i) * (1-p)**(n-i)
        return ans

    # accumulated probability
    else:
        return choose(n,x) * (p**x) * (1-p)**(n-x)
